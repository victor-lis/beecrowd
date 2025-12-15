# horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

# horas = horaFinal - horaInicial
# minutos = minutoFinal - minutoInicial

# if (minutos < 0):
#     for i in range(0, minutos, -1):
#         horas -= 1
#     minutos = 60 + minutos
    
# if (horas < 0):
#     horas = 24 + horas

# if horaInicial == horaFinal and minutoInicial == minutoFinal:
#     print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
# else:
#     print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

# não funciona corretamente