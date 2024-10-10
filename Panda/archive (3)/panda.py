import pandas as pd

db = pd.read_csv('archive (3)\DigiDB_digimonlist.csv')

#db.set_index('id', inplace=True)
#print(db.loc[9999:9999])
#print(db.head)
#print(db.tail)
#print(db.info())
#print(db.values)
#print(db.loc[0:248, ['Digimon']])

x = db.query('Stage == "Baby" & Lv50_Spd > 50')
#print(x.head())

x.to_csv('cu.csv', sep='*', index=False, encoding='utf-8-sig')
