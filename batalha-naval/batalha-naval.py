import random

# Inicio do jogo
def Inicio():

    N = int(input("Digite o Tamanho do mapa de 4 A 6: "))
    while N < 4 or N > 6:
        print("Digite um numero Valido")
        N = int(input("Digite o Tamanho do mapa de 4 A 6: "))

    print("="*40)
    print("Bem-vindo A Batalha Naval na Ilha Misteriosa")
    print()
    print("O tamanho do seu mapa sera: ", N,"X", N)
    print("="*40)

    return N

""" Construção do mapa...
Aqui preciso construir uma matriz com loops para facilitar... criar um loop para o Eixo X e Y, com
 uma logica para imprimir as cordenadas da matriz"""
def Mapa(N):


    print()

    print("-"*40)
    print ("       -- Construção do Mapa --")
    print("-"*40)
    print()

    print(end="  ")
    for i in range(N):
        print(i, end="  ")
    print()
    for j in range(N):
        print(j, end=" ")
        for h in range(N):
                print("~", end="  ")
        print()

""""Criar inimigos aleatorios pelo Mapa e escondidos"""
def Inimigos(inimigo):
    lista_inimigoR = []

    for i in range(3):
        linhax = random.randint(0, inimigo - 1)
        colunay = random.randint(0, inimigo - 1)

        lista_inimigoR.append((linhax, colunay))

    inimigo1 = lista_inimigoR[0]
    inimigo2 = lista_inimigoR[1]
    inimigo3 =lista_inimigoR[2]

    return inimigo1, inimigo2, inimigo3
    


# Base
tamanho_escolhido = Inicio()
Inimigos(tamanho_escolhido)
Mapa(tamanho_escolhido)