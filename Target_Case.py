# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma = soma + k

print(soma) # Resultado da soma é igual 91

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    sequencia = [0, 1]

    while True:
        proximo = sequencia[-1] + sequencia[-2]  # Soma os dois últimos valores
        if proximo > n:  # Se o próximo número for maior que n, quebramos o loop
            break
        sequencia.append(proximo)  # Adiciona o próximo número na variavel sequencia

    return sequencia

def pertence_fibonacci(num):
    sequencia = fibonacci(num)

    if num in sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

numero_informado = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# Dados fornecidos
dados = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Extrai os valores em uma lista
valores = [dia['valor'] for dia in dados if dia['valor'] > 0]  # Ignora valores 0 para o cálculo


# Cálculo do menor e maior valor
menor_valor = min(valores)
maior_valor = max(valores)

# Cálculo da média mensal
media_mensal = sum(valores) / len(valores) if valores else 0

# Cálculo do número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Resultados
print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor_valor:.4f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior_valor:.4f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_da_media}")


#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Faturamento mensal por estado
dados_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do total mensal
total_mensal = sum(dados_estados.values())

# Cálculo do percentual de representação de cada estado
percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in dados_estados.items()}

# Resultados
print(f"O total mensal é: R${total_mensal:.2f}")
print("\nPercentual de representação por estado:")

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# 5) Escreva um programa que inverta os caracteres de um string.

def inverte_string(string):
    return string[::-1]

palavra_informada = input('Digite uma palavra: ')
palavra_invertida = inverte_string(palavra_informada)
print(f"A string invertida é: {palavra_invertida}")


