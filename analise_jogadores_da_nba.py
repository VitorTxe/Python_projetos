import pandas as pd
import matplotlib.pyplot as plt
import seaborn

# Arquivo
arquivo = r'C:\\Users\\vitor\\Desktop\\pandas_planilhas\\01-22 - Bases de Dados para Praticar\\nba_data_processed.csv'
df = pd.read_csv(arquivo)

# Excluindo valores nulos
df = df.dropna(how='any', axis=0)

# Mudando o dtype da coluna "Age"
df['Age'] = df['Age'].astype('int16')

# Filtrando colunas
lista_colunas = ['Player', 'Pos', 'Age', 'PTS']
filtrado = df.filter(items=lista_colunas)

# Top 10 jogadores com a maior media de pontos
print('"TOP 10 PONTUADORES DA NBA"')
media_pontos = df.groupby(['Player'])['PTS'].mean()
top10_jogadores = media_pontos.sort_values(ascending=False).head(10).round(1)
print(top10_jogadores)

figura1 = plt.figure(figsize=(10, 6))
top10_jogadores = top10_jogadores.head(10).sort_values().plot(kind='barh')
top10_jogadores.bar_label(top10_jogadores.containers[0], color='black')
top10_jogadores.set_xlim(0, 40)

plt.xlabel('MÉDIA DE PONTOS')
plt.ylabel('JOGADORES')
plt.title('TOP 10 PONTUADORES', y=1.10)

plt.show()

# Quebra de linha
print()

# Top 10 jogadores mais velhos
print('"TOP 10 JOGADORES MAIS VELHOS"')
media_idade = df.groupby(['Player'])['Age'].mean()
top10_idade = media_idade.sort_values(ascending=False).head(10)
print(top10_idade)

figura2 = plt.figure(figsize=(10, 6))
top10_idade = top10_idade.head(10).sort_values().plot(kind='barh')
top10_idade.bar_label(top10_idade.containers[0], color='black')
top10_idade.set_xlim(0, 50)
plt.xlabel('IDADE')
plt.ylabel('JOGADORES')
plt.title('TOP 10 JOGADORES MAIS VELHOS', y=1.10)

plt.show()