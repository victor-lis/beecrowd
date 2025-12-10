x, y = map(float, input().split())

regras = {
    "Eixo X": y == 0 and x != 0,
    "Eixo Y": x == 0 and y != 0,
    "Q1": x > 0 and y > 0,
    "Q2": x < 0 and y > 0,
    "Q3": x < 0 and y < 0,
    "Q4": x > 0 and y < 0,
    "Origem": x == 0 and y == 0
}

for resultado, condicao in regras.items():
    if condicao:
        print(resultado)
        break