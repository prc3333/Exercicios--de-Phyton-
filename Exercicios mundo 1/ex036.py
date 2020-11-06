from time import sleep
casa = float(input('Qual e o valor da casa? R$ '))
sal = float(input('Qual e o valor do seu salário? R$ '))
an = int(input('Em quantos anos de financiamento ? '))
prest = casa / (an * 12)
mínimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, an), end=' 1')
print('A prestação será de {:.2f}'.format(prest))
sleep(3)
if prest <= mínimo:
    print('Emprestimo pode ser  concedido!!!')
else:
    print('Emprestimo Negado!!!')
