import json

with open('dados.json') as f:
    dados = [d for d in json.load(f) if d['valor'] > 0]  # Ignora dias com valor 0

valores = [d['valor'] for d in dados]
media = sum(valores) / len(valores)

print(f"Menor valor: {min(valores):.2f} (dia {min(dados, key=lambda x: x['valor'])['dia']})")
print(f"Maior valor: {max(valores):.2f} (dia {max(dados, key=lambda x: x['valor'])['dia']})")
print(f"Dias acima da média: {sum(1 for v in valores if v > media)} dias")