import pandas as pd
import numpy as np
import limpa_tela as lt
import datetime

lt.limpa_tela()

dataset = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';')

dataset2 = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';', index_col = 'Nome') # Usa a coluna nome como chave da tabela

dataset["Km_media"] = (dataset.Quilometragem/(2019-dataset.Ano)).fillna(0)

#print(dataset[['Km_media','Quilometragem']])


#Carro ano > 2013 motor diesel e com km_media <20.000

filtro = (dataset.Ano > 2013) & ((dataset.Motor =='Motor Diesel') | (dataset.Motor =='Motor Diesel V6')) & (dataset.Km_media < 20000)

# OU

dq = dataset.query("Ano > 2013 and (Motor == 'Motor Diesel' or Motor == 'Motor Diesel V6')and Km_media < 20000")

print(dataset[filtro])

print(dq)