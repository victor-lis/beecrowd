lista = list(map(float, input().split()))

lista.sort(reverse=True)
A, B, C = tuple(lista)

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if (A ** 2 == (B ** 2 + C ** 2)):
        print("TRIANGULO RETANGULO")
    if (A ** 2 > (B ** 2 + C ** 2)):
        print("TRIANGULO OBTUSANGULO")
    if (A ** 2 < (B ** 2 + C ** 2)):
        print("TRIANGULO ACUTANGULO")
    if (A == B and B == C):
        print("TRIANGULO EQUILATERO")
    if ((A == B and B != C) or (A == C and B != C) or (B == C and A != B)):
        print("TRIANGULO ISOSCELES")