comeco, fim = map(int, input().split())

tempo = 0

if fim < comeco:
    tempo = 24 - (comeco - fim)
elif fim == comeco:
    tempo = 24
else:
    tempo = fim - comeco
    
print(f'O JOGO DUROU {tempo} HORA(S)')