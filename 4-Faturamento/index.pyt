# Valor de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total do faturamento mensal
total_faturamento = sum(faturamento.values())

# Calcula o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentuais[estado] = (valor / total_faturamento) * 100

# Exibe os resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
