#O algoritmo e o código a seguir foram criados em função do exercicio de calculo de matrizes pedido em sala de aula
#A matriz escolhida foi de ordem 3x3

#    Criar matriz_a[3][3]
#    Para linha de 0 até 2:
#        Para coluna de 0 até 2:
#            Escreva "Digite o valor para a posição [", linha, ",", coluna, "] da matriz A:"
#            Leia matriz_a[linha][coluna]

#    Para linha de 0 até 2:
#        Para coluna de 0 até 2:
#            Escreva "[", matriz_a[linha][coluna], "]"
#        Escreva nova linha

#    Criar matriz_b[3][3]
#    Para linha de 0 até 2:
#        Para coluna de 0 até 2:
#            Escreva "Digite o valor para a posição [", linha, ",", coluna, "] da matriz B:"
#            Leia matriz_b[linha][coluna]

#    Para linha de 0 até 2:
#        Para coluna de 0 até 2:
#            Escreva "[", matriz_b[linha][coluna], "]"
#        Escreva nova linha

#    Escreva "Escolha uma operação: 1 para soma, 2 para subtração, 3 para multiplicação elemento a elemento"
#    Leia escolha
#    Criar resultado[3][3]

#    Se escolha = 1 então:
#        Para linha de 0 até 2:
#            Para coluna de 0 até 2:
#                resultado[linha][coluna] ← matriz_a[linha][coluna] + matriz_b[linha][coluna]
#        Escreva "Resultado da soma:"
    
#    Senão se escolha = 2 então:
#        Para linha de 0 até 2:
#            Para coluna de 0 até 2:
#                resultado[linha][coluna] ← matriz_a[linha][coluna] - matriz_b[linha][coluna]
#        Escreva "Resultado da subtração:"
    
#    Senão se escolha = 3 então:
#        Para linha de 0 até 2:
#            Para coluna de 0 até 2:
#                resultado[linha][coluna] ← matriz_a[linha][coluna] * matriz_b[linha][coluna]
#        Escreva "Resultado da multiplicação:"
    
#    Senão:
#        Escreva "Opção inválida"
#       Encerrar programa

#    Para linha de 0 até 2:
#        Para coluna de 0 até 2:
#          Escreva "[", resultado[linha][coluna], "]"
#       Escreva nova linha

matriz_a = [[0,0,0], [0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz_a [l] [c] = int(input(f'Digite um valor para [{l}, {c}] da matriz A: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz_a[l][c]:^5}]', end='')
    print()
print('-=' * 30)

matriz_b = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3): #o k representa as linhas da matriz B
    for c in range(0,3):#o v representa as colunas da matriz B
        matriz_b [l] [c] = int(input(f'Digite um valor para [{l}, {c}] da matriz B: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz_b[l][c]:^5}]', end='')
    print()
print('-=' * 30)

escolha=int(input("Você quer somar(1), subtrair(2) ou multiplicar(3) as matrizes?: "))

resultado = [[0,0,0],[0,0,0],[0,0,0]]

if escolha==1:
    for l in range(3):
        for c in range(3):
            resultado[l][c] = matriz_a[l][c] + matriz_b[l][c]
    print("Resultado da soma:")
elif escolha==2:
    for l in range(3):
        for c in range(3):
            resultado[l][c] = matriz_a[l][c] - matriz_b[l][c]
    print("Resultado da subtração:")
elif escolha==3:
    for l in range(3):
        for c in range(3):
            resultado[l][c] = matriz_a[l][c] * matriz_b[l][c]
    print("Resultado da multiplicação:")
else:
    print("Opção inválida!")

for l in range(3):
    for c in range(3):
        print(f'[{resultado[l][c]:^5}]', end='')
    print()
