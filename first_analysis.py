import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat
df = pd.read_excel('ap2020-anonymized.xlsx')

#print(df)
# Počet řádků a sloupců:
#print(df.shape)

# Informace o sloupcích:
#print(df.info())

# Nejvyšší x nejmenší příchozí ročníky:
#counts = df['ročník'].value_counts()
#print(counts)

# Kam byli příchozí pacienti odesláni nejčastěji
#place = df['odeslán'].value_counts()
#print(place)

#Kdo měl nejvíce služeb
#shifts = df['lékař'].value_counts()
#print(shifts)



# Přejmenování sloupce "datum a čas" na "datetime"
df = df.rename(columns={'datum a čas': 'datetime'})
# Převod sloupce "datetime" na typ dat timestamp
df['timestamp'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')


# Převod sloupce s timestampy na sloupec s dny v týdnu
# df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
# counts = df['day_of_week'].value_counts()
# fig, ax = plt.subplots() #slouží k vytvoření nového obrázku (fig) a jedné nebo více os (ax). Funkce subplots() vrací n-tici obsahující odkazy na figuru a na osy, které jsou vytvořeny, kde "n" závisí na počtu řádků a sloupců grafu.
# ax.bar(counts.index, counts.values)
# ax.set_xticks(range(7))
# ax.set_xticklabels(['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle'])
# ax.set_ylabel('Počet pacientů v roce 2020')
# ax.set_xlabel('Den v týdnu')
# plt.show()



# Převod sloupce s timestampy na sloupec s hodinami
#df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

# Výpočet počtu výskytů každé hodiny
#counts = df['hour'].value_counts()

# Vykreslení grafu s počtem výskytů pro každou hodinu
# fig, ax = plt.subplots()
# ax.bar(counts.index, counts.values, color = 'red')
# ax.set_xticks(range(24))
# ax.set_xlabel('Hodina')
# ax.set_ylabel('Počet pacientů v roce 2020')
# plt.show()


# Převod sloupce s timestampy na sloupec s měsícem
df['month'] = pd.to_datetime(df['timestamp']).dt.month
#
# Výpočet počtu výskytů každý měsíc
counts = df['month'].value_counts()
#
# Vykreslení grafu s počtem výskytů pro každý měsíc
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values, color = 'red')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec'])
ax.set_xlabel('Měsíc')
ax.set_ylabel('Počet pacientů v roce 2020')
plt.show()