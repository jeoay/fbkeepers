import sqlite3

def main():
    db = sqlite3.connect('keepers.db')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists keepers')
    db.execute('create table keepers (Player text, Position text, DraftRd16 int, OvrProj17 int)')
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Manny Machado', '3B/SS', 10, 7))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Starling Marte', 'OF', 4, 18))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('George Springer', 'OF', 3, 26))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Jonathan Lucroy', 'C/1B', 7, 98))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('DJ LeMahieu', '2B', 13, 101))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('José Ramírez', '3B/OF', 0, 169))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Nelson Cruz', 'OF', 3, 32))
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Miguel Sano', '3B/OF', 24, 151))    
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Willson Contreras', 'C/OF', 0, 111))    
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Blake Snell', 'SP', 0, 252))    
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Chris Archer', 'SP', 11, 65))    
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Rick Porcello', 'SP', 18, 99))    
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Danny Duffy', 'SP', 0, 125))        
    db.execute('insert into keepers (Player, Position, DraftRd16, OvrProj17) values (?, ?, ?, ?)', ('Trevor Story', 'SS', 14, 37))    
            
    db.commit()
    cursor = db.execute('select * from keepers order by OvrProj17')
    for row in cursor:
        #print(dict(row)) ### prints in a dictonary
        #print(row['Player'], row['Position'], row['DraftRd16'], row['OvrProj17']) ### prints out indivdual rows
        proj_rd17 = row['OvrProj17'] / 12 + 1
        print(row['Player'], '(' + row['Position'] + ')')
        print('Proj Rd:' + str(int(proj_rd17)))
        print('2016 Draft Rd:', row['DraftRd16'])
        if row['DraftRd16'] == 0:
            print('Give up last round pick to keep player')
        else:
            print('Give up {} round pick to keep player'.format(row['DraftRd16'] - 1))
        print('')
        
if __name__ == "__main__": main()