import pandas as pd
import numpy as np
import limpa_tela as lt

lt.limpa_tela()

## Queries dataframe
dataset = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';')

info = dataset.info()

print(info) #Veja que o campo Quilometragem tem menos dados que as demais colunas.

validaQuilometragem = dataset['Quilometragem'].isna()

# print(validaQuilometragem)

#filtro = dataset['Quilometragem'].isna()

#dataset.fillna(0, inplace= True)  #Trocou o NaN por 0.00 (Zero)

#print(dataset[filtro])

#print(dataset)

dfna = dataset.dropna(subset=['Quilometragem'])

filtroOrdemCrescente = dfna.sort_values(by= "Valor", ascending= True)

filtroOrdemDerescente = dfna.sort_values(by= "Valor", ascending= False)

agrupamento = dataset.groupby(by=["Motor"])["Valor"].describe().sort_values(by="mean", ascending=False)

# media = agrupamento["Valor"].mean()

print(agrupamento)

# Agrupar por Ano, calcular estatistica descritiva por quilometragem e ordenar pela media da quilometragem

agrupamentoAno = dataset.groupby(by=["Ano"])["Quilometragem"].describe().sort_values(by="mean", ascending=False)

print(agrupamentoAno)