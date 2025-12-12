casos = int(input())

for i in range(casos):
    f1, f2 = map(int, input().split())
    divisores = []
    
    for numero in range(1, min([f1, f2])):
        if (f1 % numero == 0) and (f2 % numero == 0):
            divisores.append(numero)
    print(max(divisores))