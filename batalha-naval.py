# Inicio do jogo
def Inicio():

    N = int(input("Digite o Tamanho do mapa de 4 A 6: "))
    while N < 4 or N > 6:
        print("Digite um numero Valido")
        N = int(input("Digite o Tamanho do mapa de 4 A 6: "))

    print("="*40)
    print("Bem-vindo AO Batalha Naval na Ilha Misteriosa")
    print("O tamanho do seu mapa sera: ", N)
    print("="*40)

    return N

""" Construção do mapa...
Aqui preciso construir uma matriz com loops para facilitar... criar um loop para o Eixo X e Y, com uma logica para imprimir as cordenadas da matriz"""
N = Inicio()

print(end="  ")
for i in range(N):
    print(i, end="  ")
print()
for j in range(N):
    print(j)