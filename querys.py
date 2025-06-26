import pandas as pd
import numpy as np
import limpa_tela as lt

lt.limpa_tela()

## Queries dataframe
dataset = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';')

dataset2 = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';', index_col = 'Nome') # Usa a coluna nome como chave da tabela

print(dataset2.Motor) # Mesa coisa que print(dataset2["Motor"])

print(dataset.Motor == "Motor Diesel") # Mostra quem é igual a Motor diesel

print(dataset.Motor != "Motor Diesel") # Mostra quem é diferente a Motor diesel

lt.limpa_tela()

filtro = (dataset.Motor == "Motor Diesel") & (dataset.Zero_km == True)
df = dataset[filtro]
print(df)

lt.limpa_tela()

dq = dataset.query('(Motor == "Motor Diesel") and (Zero_km == False) and (Ano >2013)') ## na query deve-se usar diretamente o nome do campo sem referenciar ao dataset
print(dq)

