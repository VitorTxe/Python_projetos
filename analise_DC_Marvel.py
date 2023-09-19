import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# pd.set_option('display.max_columns',None)

arquivo = r'C:\Users\vitor\Desktop\pandas_planilhas\01-22 - Bases de Dados para Praticar\comic_characters.csv'
df = pd.read_csv(arquivo)

# Mudando os valores da coluna Alive
df.loc[df['Alive'] == 'No', 'Alive'] = 'Mortos'
df.loc[df['Alive'] == 'Yes', 'Alive'] = 'Vivos'

# Tamanho do dataframe
print(df.shape)
print()

# Verificando as 10 primeiras linhas da tabela
print(df.head(10))
print()

# Verificando dtype de cada coluna e quanto de memória esta sendo usado
print(df.info())
print()

# Verificando se há dados nulos
print(df.isnull().sum())
print()

# Mudando o dtype de Object para Category
coluna_object = ['Identity', 'Alignment', 'Sex', 'Alive', 'Universe']
df[coluna_object] = df[coluna_object].astype('category')

# Mudando os dtupe de Int64 para Int16
coluna_int = list(df.select_dtypes(include='int').columns)
df[coluna_int] = df[coluna_int].astype('int16')

# Verificando se os dados foram mudados e quanto de memória está sendo usado
print(df.info())
print()

# Personagens separados por gênero
col_filtrado = df[['Name', 'Identity', 'Alignment', 'Sex', 'Alive', 'Universe']]
marvel_herois = col_filtrado.groupby(['Universe', 'Sex'])['Name'].count()
print(marvel_herois)
print()

# Quantos herois, viloes temos nos dois universos
agrupando = col_filtrado.groupby(['Universe', 'Alignment'])['Name'].count()
print(agrupando)
print()

# Visualizando qual universo tem mais personagens
plt.figure(figsize=(6, 6))
ax = sns.countplot(data=col_filtrado, x='Universe', palette='winter')
plt.ylabel('Número de personagem')
plt.title('Personagens do universo DC e Marvel', y=1.10)
ax.bar_label(ax.containers[0], color='black')
sns.despine(left=True, bottom=False)
plt.ylabel('')
plt.yticks([])
plt.show()

# Visualizando as personalidades dos personagens da Marvel
plt.figure(figsize=(6, 6))
filtro_marvel = col_filtrado.loc[col_filtrado['Universe'] == 'Marvel']
grafico_marvel = sns.countplot(data=filtro_marvel, x='Alignment', palette='winter')
grafico_marvel.bar_label(grafico_marvel.containers[0], color='black')
plt.title('Personalidade dos personagens da Marvel', y=1.10)
sns.despine(left=True, bottom=False)
plt.ylabel('')
plt.yticks([])
plt.show()

# Visualizando as personalidades dos personagens da DC
plt.figure(figsize=(6, 6))
filtro_dc = col_filtrado.loc[col_filtrado['Universe'] == 'DC']
grafico_dc = sns.countplot(data=filtro_dc, x='Alignment', palette='winter')
grafico_dc.bar_label(grafico_dc.containers[0], color='black')
sns.despine(left=True, bottom=False)
plt.title('Personalidades dos personagens da DC', y=1.10)
plt.ylabel('')
plt.yticks([])
plt.show()

# Comparando quantos vilões estao vivos e mortos no universo DC e Marvel
alive_dc = col_filtrado.loc[(col_filtrado['Universe'] == 'DC') & (col_filtrado['Alignment'] == 'Bad')]
alive_marvel = col_filtrado.loc[(col_filtrado['Universe'] == 'Marvel') & (col_filtrado['Alignment'] == 'Bad')]
fig, grafico = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))

sns.countplot(data=alive_dc, x='Alive', palette='winter', ax=grafico[0])
sns.countplot(data=alive_marvel, x='Alive', palette='winter', ax=grafico[1])

grafico[0].set_title('DC - Vilões', y=1.10)
grafico[0].bar_label(grafico[0].containers[0], color='black')
grafico[1].set_title('Marvel - Vilões ', y=1.10)
grafico[1].bar_label(grafico[1].containers[0], color='black')
grafico[1].set_ylim(0, 10000)
sns.despine(left=True, bottom=False)
grafico[0].set_ylabel('')
grafico[0].set_xlabel('')
grafico[0].set_yticks([])
grafico[1].set_xlabel('')
grafico[1].set_ylabel('')
grafico[1].set_yticks([])


plt.tight_layout()
plt.show()














