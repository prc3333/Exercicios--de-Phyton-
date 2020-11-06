from time import sleep
velocidade = float(input('Qual e a sua velocidade atual? '))
if velocidade > 80:
    print('Voce esta a {}KM/h e acima da velocidade permitida que e 80KM/h e foi multado!'.format(velocidade))
    print('Aguarde para ser informado sobre o valor da multa!')
    sleep(2)
    multa = (velocidade - 80) * 7
    print('O valor de sua multa e de R${}'.format(multa))
print('Tenha um Bom Dia!\nE dirija com segurança!!!')








