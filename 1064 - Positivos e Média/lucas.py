valores = []
for _ in range(6):
    valor = float(input())
    if valor > 0:
        valores.append(valor)
        
print(f"{len(valores)} valores positivos")
print(f"{sum(valores)/len(valores):.1f}")
