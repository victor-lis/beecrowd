notas = list(map(float, input().split()))

ponderadas = {
    0: 2,
    1: 3,
    2: 4,
    3: 1
}

mediaFinal = 0

for indice, media in ponderadas.items():
    
    notaPonderada = notas[indice] * media
    mediaFinal += notaPonderada 
    
    
mediaFinal = mediaFinal / 10
print(f"Media: {mediaFinal:.1f}")

if mediaFinal >= 7:
    print("Aluno aprovado.")
elif mediaFinal >= 5 and mediaFinal < 7:
    
    print("Aluno em exame.")
    notaExame = float(input())
    print(f"Nota do exame: {notaExame:.1f}")   
    if ((notaExame + mediaFinal) / 2) >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
            
    print(f"Media final: {((notaExame + mediaFinal) / 2):.1f}")
else:
    print("Aluno reprovado.")
         