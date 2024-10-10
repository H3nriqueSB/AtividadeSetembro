import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("archive (3)/DigiDB_digimonlist.csv")

#plt.plot(1, 2, 3, 4, 5),(1, 4, 9, 15, 59)
#plt.plot((1, 2, 3, 4, 5),(1, 4, 9, 15, 59), "mo")

plt.bar((1, 2, 3, 4, 5),(1, 4, 9, 15, 59))
plt.ylabel(u'HP')
plt.xlabel(u'Def')
plt.title('Digimon')

plt.show()