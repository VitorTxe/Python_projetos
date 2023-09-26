import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega todas as colunas e linhas da tabela 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Dataframe
arquivo = r'C:\Users\vitor\Desktop\pandas_planilhas\ign.csv'
df = pd.read_csv(arquivo)

# Selecionandos colunas especificas para a analise
colunas = ['score_phrase', 'title', 'platform', 'score', 'genre', 'editors_choice', 'release_year', 'release_month']
coluna_filtrada = df.filter(items=colunas)

# Mudando os nomes das colunas selecionadas
novos_nomes = ['status', 'titulo', 'plataforma', 'score', 'genero', 'escolha dos editores', 'ano de lançamento', 'mes']
coluna_filtrada.columns = novos_nomes

# Verificando se há valores vazios no dataframe
dados_nulos = coluna_filtrada.isna().sum()
print(dados_nulos)

# Mudando os valores vazios
coluna_filtrada['genero'] = coluna_filtrada['genero'].fillna('Sem genero')

# Vericando se a mudança deu certo
dados_nulos = coluna_filtrada.isna().sum()
print(dados_nulos)

# Informaçoes sobre as colunas selecionas
print(coluna_filtrada.info())

# Mudando os valores de object para category
colunas_type = {
    'status': 'category',
    'plataforma': 'category',
    'genero': 'category',
    'score': 'int16',
    'escolha dos editores': 'category',
    'ano de lançamento': 'int16'
}
coluna_filtrada = coluna_filtrada.astype(colunas_type)
print(coluna_filtrada.info())

# Quebra de linha
print()

# Média da nota dos jogos por plataforma
print('"Média da nota dos jogos por plataforma"\n')
media_nota = coluna_filtrada.groupby(['plataforma'])['score'].mean().round(1).sort_values(ascending=False)
print(media_nota)

# Top 10 média dos jogos por plataforma
plt.figure(figsize=(12, 6))
media_nota = media_nota.head(10).sort_values().plot(kind='barh')
plt.title('Top 10 plataformas com maiores médias', y=1.10)
media_nota.bar_label(media_nota.containers[0], color='black')
plt.xlabel('Nota')
plt.xlim(0, 10, 2)
plt.show()

# Quebra de linha
print()

# Média da nota por genero
print('"Média da nota por genero"\n')
media_genero = coluna_filtrada.groupby(['genero'])['score'].mean().round(1).sort_values(ascending=False)
print(media_genero)

# Top 10 média por genero
plt.figure(figsize=(15, 6))
media_genero = media_genero.head(10).sort_values().plot(kind='barh')
media_genero.bar_label(media_genero.containers[0], color='black')
plt.title('Top 10 generos com as maiores médias', y=1.10)
plt.xlabel('Nota')
plt.xlim(0, 10, 2)
plt.show()

# Lançamentos de jogos por ano
print('"Lançamentos de jogos por ano\n"')
ano_lancamento = coluna_filtrada.groupby(['ano de lançamento'])['titulo'].count()
print(ano_lancamento)

# Gráfico lançamentos de jogos por ano
plt.figure(figsize=(15, 6))
sns.barplot(x=ano_lancamento.index, y=ano_lancamento.values)
plt.title('Lançamentos de jogos por ano', y=1.10)
plt.xlabel('')
plt.ylabel('Quantidade de jogos')
plt.show()

# Transformando número dos meses no seu respectivo nome
meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

coluna_filtrada['mes'] = coluna_filtrada['mes'].map(meses)

# Lançamentos de jogos por mês
print('"Lançamentos de jogos por mês"\n')
mes_lancamento = coluna_filtrada.groupby(['mes'])['titulo'].count().sort_values(ascending=False)
print(mes_lancamento)

# Gráfico - Lançamentos de jogos por mês
plt.figure(figsize=(15, 6))
ordena_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
grafico_mes = sns.countplot(data=coluna_filtrada, x='mes', order=ordena_meses, color='Red')
plt.title('Lançamento de jogos por mês', y=1.10)
plt.xlabel('')
plt.xticks(rotation=45)
plt.ylabel('Quantidade jogos')
plt.ylim(0, 3000)
grafico_mes.bar_label(grafico_mes.containers[0], color='black')
plt.title('Lançamentos de jogos por mês', y=1.10)
plt.show()

# Gráfico - Escolha dos editores
plt.figure(figsize=(12, 6))
paleta_cores = {'N': 'red', 'Y': 'green'}
grafico_escolha_editores = sns.countplot(data=coluna_filtrada, x='escolha dos editores', palette=paleta_cores)
grafico_escolha_editores.bar_label(grafico_escolha_editores.containers[0], color='black')
plt.xlabel('N = Não     Y = Sim')
plt.ylabel('Quantidade de jogos')
plt.title('Quantos jogos os editores aprovam ou reprovam ?', y=1.10)
plt.ylim(0, 20000)
plt.show()

# Quebra de linha
print()

# Quantos jogos por plataforma os editores aprovam ou reprovam ?
print('"Quantos jogos por plataforma os editores aprovam ou reprovam ?"\n')
editores = coluna_filtrada.groupby(['escolha dos editores', 'plataforma'])['titulo'].count()
print(editores)
