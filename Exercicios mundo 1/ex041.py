from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento:'))
idade = atual - nascimento
print('O Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação mirim!')
elif idade <= 14:
    print('Classificação Infantil!')
elif idade <= 19:
    print('Classificação Junior!')
elif idade <= 25:
    print('Classificação Sênior!')
else:
    print('Classificação Master!')

