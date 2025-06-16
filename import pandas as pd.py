import pandas as pd
import numpy as np
import limpa_tela as lt

lt.limpa_tela()

dataset = pd.read_csv('https://raw.githubusercontent.com/daniel-usp/LIT/master/db.csv', sep=';')

print(float(dataset["Valor"].std()))




# converter um dataset em dicionario [

dict_dataset = dataset.to_dict('list')
print(dict_dataset)

df = pd.DataFrame(dict_dataset)

print(df)


#print(dataset.head(34))

#print(dataset.info)
