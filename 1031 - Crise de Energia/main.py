while True:
    numeroRegioes = int(input("N (13..100, outro para sair): "))
    if not (13 <= numeroRegioes <= 100):
        break

    # lista original (sem o 1, porque você começa com 1 já apagado)
    original = list(range(2, numeroRegioes + 1))

    tentativa = 0
    achou = False

    while not achou:
        tentativa += 1

        # recria a lista a cada tentativa a partir do original (cópia fresca)
        listaRegioes = original.copy()
        listaApagados = [1]    # estado consistente no início da tentativa
        salto = 1
        i = 0

        # simula até acabar a lista
        while listaRegioes:
            i = (i + salto) % len(listaRegioes)
            pop = listaRegioes.pop(i)
            listaApagados.append(pop)
            salto += 1

        # agora a lista acabou; checa se o último removido foi 13
        if listaApagados[-1] == 13:
            print("Tentativa:", tentativa)
            print("Ordem de remoção:", listaApagados)
            print("Encontrou — 13 foi o último.")
            achou = True
        # caso contrário, o while not achou repete automaticamente
