numeros = list(map(int, input().split()))

print("Sao Multiplos") if max(numeros) % min(numeros) == 0 else print("Nao sao Multiplos") 
