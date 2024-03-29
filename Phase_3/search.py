proximity_formula = '''
    6371*ACOS(COS(RADIANS(r.Latitude))*COS(RADIANS(ic.Latitude))*
    COS(RADIANS(r.Longitude-ic.Longitude))+SIN(RADIANS(r.Latitude))*
    SIN(RADIANS(ic.Latitude)))
AS proximity'''
ESFcond = '''(r.PrimaryESFNumber = %s OR %s IN
    (SELECT ESFNumber FROM AdditionalESF ad
        WHERE ad.ResourceID = r.ID))'''
Usable = '''NOT EXISTS
    (SELECT * FROM LastUsed
        WHERE ResourceID=r.ID and
            Abbreviation = ic.Abbreviation and
            Number=ic.Number)'''
Incident = 'JOIN (SELECT * FROM Incidents WHERE Abbreviation = %s AND Number = %s) ic'
def sql_string(keyword="", ESFNumber=None, radius=None, abbreviation=None, number=None):
    # Set basic cols, Tables and conditions
    cols = ['r.ID', 'r.Name', 'u.Name as Owner', 'r.Cost', 'r.UnitName', 'i.ReturnDate']
    tables = ['Resources r JOIN User u ON u.Username=r.Username',
              'LEFT JOIN InUse i ON r.ID = i.ResourceID']
    conditions = []
    if keyword:
        conditions.append(('''(r.Name like %s OR r.Model like %s OR EXISTS
            (SELECT * FROM Capabilities c WHERE c.ResourceID = r.ID AND c.CapabilityName like %s))''',
            ['%{}%'.format(keyword)]*3))
    if ESFNumber:
        conditions.append((ESFcond, [ESFNumber, ESFNumber]))
    tails = []
    # Change cols, Tables, conditions and tails accordingly
    if abbreviation and number is not None:
        tails.append("Having proximity <= COALESCE(MaxDistance, 100000)")
        if radius is not None:
            tails.append(('AND proximity <= %s', [radius]))
        cols.append(proximity_formula)
        cols.append('(r.Username = ic.Username) AS Own')
        cols.append('r.MaxDistance')
        tails.append('\nORDER BY proximity, r.Name ASC')
        conditions.append(Usable)
        tables.insert(1, (Incident, [abbreviation, number]))

    Q = ['SELECT', ', '.join(cols), '\nFROM', *tables]
    if conditions:
        Q += ['\nWhere', conditions[0]]
        for c in conditions[1:]:
            Q += ['AND', c]
    Q += tails
    # Convert query elements to sql with args
    sql = []
    args = []
    for i in Q:
        if isinstance(i, str):
            sql.append(i)
        else:
            sql.append(i[0])
            args += i[1]
    return '\n'.join(sql), tuple(args)
