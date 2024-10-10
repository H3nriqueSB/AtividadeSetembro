import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("archive (3)/DigiDB_digimonlist.csv")

#HP e Defesa
# defense = x['Lv50_Def']
# hp = x['Lv50_HP']

# plt.plot(defense, hp, "mD") 

# plt.ylabel(u'HP')
# plt.xlabel(u'Defense')
# plt.title('Relação entre HP e Defesa dos Digimons')

# plt.show()

#--------------------------------------------------------------------------------
#SPEED
# speed = x.groupby('Digimon')['Lv50_SP'].mean()
# Obtendo os 50 digimons mais rápidos
# top_speed = speed.nlargest(50)
# plt.bar(top_speed.index, top_speed.values)
# plt.ylabel(u'Speed')
# plt.xlabel(u'Nome')s
# plt.title('Velocidade dos 50 Digimons Mais Rápidos')
# plt.xticks(rotation=45, ha='right')

# plt.show()

#--------------------------------------------------------------------------------
#EquipSlots
# Equip = x['Equip_Slots']
# Equip = Equip.loc[50:80]
# Nome = x['Digimon']
# Nome = Nome.loc[50:80]


# plt.pie(Equip, labels=Nome) 

# plt.title('Equip Slots dos Digimons')

# plt.show()
#--------------------------------------------------------------------------------
