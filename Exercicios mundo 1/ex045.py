from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Jogador Venceu!')

    elif jogador == 2:
        print('Computador venceu!')

    else:
        print('Jogada Inválida!!!')

elif computador == 1:  # computador jogou papael
    if jogador == 0:
        print('Computador venceu!')

    elif jogador == 1:
        print('Empate')

    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada Inválida!!!')

elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('Jogador Venceu!')

    elif jogador == 1:
        print('Computador venceu!')

    elif jogador == 2:
        print('Empate')

    else:
        print('Jogada Inválida!!!')
