import pandas as pd
import numpy as np
import limpa_tela as lt

lt.limpa_tela()

dataset = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';')

dataset2 = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';', index_col = 'Nome') # Usa a coluna nome como chave da tabela

print(float(dataset["Valor"].std()))

# converter um dataset em dicionario [

#dict_dataset = dataset.to_dict('list')
#print(dict_dataset)


#converter um dicionario em dataset
#df = pd.DataFrame(dict_dataset)
#print(df)


#print(dataset.head(34))

#print(dataset.info)

filtro = ["Acessórios", "Valor"]
dataset[filtro]

subset = (dataset[filtro])
print(subset)

#mostra o nome das colunas
print(dataset.columns)

#é possível usar indices
print(dataset.columns[2]) #Ano
print(dataset.columns[4]) #Zero_km


filtro = [dataset.columns[4], dataset.columns[5]]
dataset[filtro]

subset = (dataset[filtro])
print(subset)

#Selecionando linhas e colunas 
print(dataset[1:3]) # segunda e terceiras linhas do dataset
print("")
print(dataset[0:5]) #5 primeiras linhas do dataset
#ou
print("")
print(dataset.head(5))

#Usando dataset2 para estudar LOC

print(dataset2.loc[['Passat', 'DS5', 'Macan']])

lt.limpa_tela()


# transformo em dataframe e imprimo nome, motor e valor
df = dataset2.loc[['Passat','DS5'],['Motor','Valor']]

df2 = dataset2.loc[:,['Motor','Valor']] #pega todas as linhas sem excessão

print(df)
print(df2)
lt.limpa_tela()

# UTILIZANDO iloc

print(dataset2.iloc[[0, 1, 2, 3 ]])

print(dataset2.iloc[[0, 1],[3,4]])

print("")
print(dataset2.iloc[0:3,0:3]) #pegou 3 primeiras linhas e 3 primeiras colunas da tabela

print("")

print(dataset2.iloc[0:3,[1,0]]) #inverte a ordem das colunas Ano passou a vir na frente