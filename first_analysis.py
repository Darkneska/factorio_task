import pandas as pd

# Data read
df = pd.read_excel('ap2020-anonymized.xlsx')

# Counts of rows and columns
#print(df.shape)

# Informations about columns
#print(df.info())

# Description of data set
print(df.describe())