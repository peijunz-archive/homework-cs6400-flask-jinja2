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
    cols = ['r.ID', 'r.Name', 'u.Name as Owner', 'r.Cost', 'r.UnitName', 'CAST(i.ReturnDate AS DATE)']
    tables = ['Resources r JOIN User u ON u.Username=r.Username',
              'LEFT JOIN InUse i ON r.ID = i.ResourceID']
    conditions = []
    if keyword:
        conditions.append(('r.Name like %s', ['%{}%'.format(keyword)]))
    if ESFNumber:
        conditions.append((ESFcond, [ESFNumber, ESFNumber]))
    tails = []
    # Change cols, Tables, conditions and tails accordingly
    if abbreviation and number is not None:
        if radius:
            tails.append(('Having proximity < %s', [radius]))
        cols.append(proximity_formula)
        cols.append('(r.Username = ic.Username) AS Own')
        tails.append('ORDER BY proximity, r.Name ASC')
        conditions.append(Usable)
        tables.insert(1, (Incident, [abbreviation, number]))

    Q = ['SELECT', ', '.join(cols), 'FROM', *tables]
    if conditions:
        Q += ['Where', conditions[0]]
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

def sql_format(s, args):
    args = tuple(repr(i) for i in args)
    return s%args
