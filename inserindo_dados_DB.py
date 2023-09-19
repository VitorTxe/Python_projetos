import pymysql
from faker import Faker
import random

# Crie uma instância do Faker
fake = Faker()

# Conexao com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='aaa148990',
    database='python'
)

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

materia = ['matematica', 'fisica', 'historia', 'ciencia', 'portugues', 'geografia']
escolha = ['m', 'f']

# Gerar e inserir dados fictícios
for i in range(100):
    nome = fake.first_name()
    sobrenome = fake.last_name()
    idade = random.randint(18, 80)
    sexo = random.choice(escolha)
    materia_random = random.choice(materia)
    nota = random.randint(0, 100)

    query = "INSERT INTO escola (nome, sobrenome, idade, sexo, materia, nota) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (nome, sobrenome, idade, sexo, materia_random, nota)
    cursor.execute(query, data)

# Salvando as todas as alterações
conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

print("Inserção de dados concluída.")
