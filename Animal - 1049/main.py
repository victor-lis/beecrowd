animais = [
    ("vertebrado", "ave", "carnivoro", "aguia"),
    ("vertebrado", "ave", "onivoro", "pomba"),
    ("vertebrado", "mamifero", "onivoro", "homem"),
    ("vertebrado", "mamifero", "herbivoro", "vaca"),
    ("invertebrado", "inseto", "hematofago", "pulga"),
    ("invertebrado", "inseto", "herbivoro", "lagarta"),
    ("invertebrado", "anelideo", "hematofago", "sanguessuga"),
    ("invertebrado", "anelideo", "onivoro", "minhoca"),
]

condicoes = []
for _ in range(3):
    condicoes.append(input())

def pegar_animal():
    for animal in animais:
        if condicoes[0] in animal and condicoes[1] in animal and condicoes[2] in animal:
            print(animal[-1])
            break
        
pegar_animal()