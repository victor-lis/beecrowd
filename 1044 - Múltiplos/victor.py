menor, maior = map(int, input().split())

if maior > menor:
    print("Sao Multiplos" if maior % menor == 0 else "Nao sao Multiplos")
else: 
    print("Sao Multiplos" if menor % maior == 0 else "Nao sao Multiplos")