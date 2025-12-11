notas = list(map(float, input().split()))

pesoMaximo = 2+3+4+1
ponderadas = [
    notas[0] * 2,
    notas[1] * 3,
    notas[2] * 4,
    notas[3] *1,
]

media = sum(ponderadas) / pesoMaximo

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    mediaFinal = (exame + media) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {mediaFinal:.1f}")