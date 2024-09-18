import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de gráficos
import seaborn  # Importa a biblioteca seaborn para visualização de dados, mas não usada neste código

# Define o caminho do arquivo CSV que contém os dados da NBA
arquivo = r'C:\Users\vitor\Desktop\pandas_planilhas\01-22 - Bases de Dados para Praticar\nba_data_processed.csv'
df = pd.read_csv(arquivo)  # Lê o arquivo CSV e armazena os dados no DataFrame 'df'

# Excluindo valores nulos
df = df.dropna(how='any', axis=0)  # Remove quaisquer linhas que contenham valores nulos

# Mudando o dtype da coluna "Age"
df['Age'] = df['Age'].astype('int16')  

# Filtrando colunas
lista_colunas = ['Player', 'Pos', 'Age', 'PTS']  
filtrado = df.filter(items=lista_colunas)  # Cria um novo DataFrame com apenas as colunas filtradas

# Top 10 jogadores com a maior média de pontos
print('"TOP 10 PONTUADORES DA NBA"')  # Exibe uma mensagem de cabeçalho no console
media_pontos = df.groupby(['Player'])['PTS'].mean()  # Agrupa os dados por 'Player' e calcula a média de pontos
top10_jogadores = media_pontos.sort_values(ascending=False).head(10).round(1) # Organiza os jogadores pela média de pontos em ordem decrescente e seleciona os 10 primeiros
print(top10_jogadores)  # Exibe os 10 jogadores com a maior média de pontos no console

# Cria uma nova figura para o gráfico
figura1 = plt.figure(figsize=(10, 6))  # Define o tamanho da figura do gráfico
top10_jogadores = top10_jogadores.head(10).sort_values().plot(kind='barh')  # Cria um gráfico horizontal de barras
top10_jogadores.bar_label(top10_jogadores.containers[0], color='black')  # Adiciona rótulos às barras com a média de pontos
top10_jogadores.set_xlim(0, 40)  # Define o limite do eixo x de 0 a 40

# Define o rótulo do eixo x
plt.xlabel('MÉDIA DE PONTOS')
# Define o rótulo do eixo y
plt.ylabel('JOGADORES')
# Define o título do gráfico
plt.title('TOP 10 PONTUADORES', y=1.10)

# Exibe o gráfico
plt.show()

# Quebra de linha
print()  

# Top 10 jogadores mais velhos
print('"TOP 10 JOGADORES MAIS VELHOS"')  # Exibe uma mensagem de cabeçalho no console
media_idade = df.groupby(['Player'])['Age'].mean()  # Agrupa os dados por 'Player' e calcula a média de idade
top10_idade = media_idade.sort_values(ascending=False).head(10) # Organiza os jogadores pela média de idade em ordem decrescente e seleciona os 10 primeiros
print(top10_idade)  # Exibe os 10 jogadores mais velhos no console

# Cria uma nova figura para o gráfico
figura2 = plt.figure(figsize=(10, 6))  # Define o tamanho da figura do gráfico
top10_idade = top10_idade.head(10).sort_values().plot(kind='barh')  # Cria um gráfico horizontal de barras
top10_idade.bar_label(top10_idade.containers[0], color='black')  # Adiciona rótulos às barras com a média de idade
top10_idade.set_xlim(0, 50)  # Define o limite do eixo x de 0 a 50

# Define o rótulo do eixo x
plt.xlabel('IDADE')
# Define o rótulo do eixo y
plt.ylabel('JOGADORES')
# Define o título do gráfico
plt.title('TOP 10 JOGADORES MAIS VELHOS', y=1.10)

# Exibe o gráfico
plt.show() 
