salário = float(input('Qual e o salário do funcionário?R$:'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.3f}'.format(salário, novo))