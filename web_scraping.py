from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import math

# Link do site
url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
# Pegando o header da maquina para nao da ser barrado do site
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

# Requisição do site, se der certo retornará reponse[200]
site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

# Localiza quantos produtos tem no total
qtd_itens = soup.find('div', id='listingCount').get_text().strip()

# Deixa aparecendo apenas o numero de produtos "900"
index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

# Calcula quantas páginas há
ultima_pagina = math.ceil(int(qtd)/20)

# Cria um dicionario com o titulo e o preço dos produtos
dict_produtos = {'marca': [], 'preço': []}

# Iterando sobre as páginas do site
for i in range(1, ultima_pagina + 1):
    url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    # Iterando sobre todos os produtos por página
    for produto in produtos:
        marca = soup.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = soup.find('span', class_=re.compile('priceCard')).get_text().strip()

        print(marca, preco)

        dict_produtos['marca'].append(marca)
        dict_produtos['preço'].append(preco)

# Cria um Dataframe
df = pd.DataFrame(dict_produtos)
df.to_excel(r'C:\Users\vitor\Desktop\pandas_planilhas\Preço_cadeiras.xlsx')