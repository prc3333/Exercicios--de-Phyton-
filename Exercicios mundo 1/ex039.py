from datetime import date
from time import sleep
nasc = int(input('Em que ano voce nasceu? '))
idade = date.today().year - nasc
falta = 18 - idade
passou = idade - 18
print('Analisando sua situação...')
sleep(3)
if idade <= 17:
    print('você tem {} anos e ainda faltam {} anos para você se alistar'.format(idade, falta))

elif idade == 18:
    print(' você tem {} anos.Está na hora de se alistar'.format(idade))

else:
    print('Você tem {} anos e ja se passaram {} anos que voce deveria ter se alistado'.format(idade, passou))


