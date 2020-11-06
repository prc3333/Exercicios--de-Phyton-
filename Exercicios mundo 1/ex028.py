from random import randint
from time import sleep
print('-=-' * 12)
print('vou pensar em um numero entre 0 e 5 tente advinhar ')
print('-=-' * 12)
jogador = int(input('Qual foi o numero que pensei? '))
computador = randint(0, 5)
print('Processando....')
sleep(2)
if jogador == computador:
    print('Parabéns voce acertou!!!, o numero que pensei foi {}'.format(computador))
else:
    print('Que Pena você errou!!,o numero que pensei foi {}'.format(computador))


