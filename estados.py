faturamento = {
    "SP": 67836.43,
    "RJ": 36078.98,
    "MG": 29229.88,
    "ES": 27105.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")