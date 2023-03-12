import json

# Lê o arquivo JSON com os dados de faturamento diário
with open('faturamento.json') as file:
    dados_faturamento = json.load(file)

# Inicializa as variáveis para os valores mínimo e máximo de faturamento
faturamento_minimo = float('inf')
faturamento_maximo = float('-inf')

# Calcula a média de faturamento, desconsiderando os dias sem faturamento
faturamento_total = 0
dias_com_faturamento = 0
for dia in dados_faturamento['faturamento']:
    if dia > 0:
        faturamento_total += dia
        dias_com_faturamento += 1
        if dia < faturamento_minimo:
            faturamento_minimo = dia
        if dia > faturamento_maximo:
            faturamento_maximo = dia
faturamento_medio = faturamento_total / dias_com_faturamento

# Calcula o número de dias com faturamento acima da média
dias_acima_da_media = 0
for dia in dados_faturamento['faturamento']:
    if dia > faturamento_medio:
        dias_acima_da_media += 1

# Exibe os resultados
print(f"Menor valor de faturamento: R${faturamento_minimo:.2f}")
print(f"Maior valor de faturamento: R${faturamento_maximo:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
