print('-' * 15)
print('LOJA DO PAULO')
print('-' * 15)
total = totmil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: '))
    prec = float(input('Preço: R$ '))
    cont += 1
    total += prec
    if prec > 1000:
        totmil += 1
    if cont == 1 or prec < menor:
        menor = prec
        barato = prod
    '''else:
        if prec < menor:
            menor = prec
            barato = prod'''
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim Do Programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que  custa R${menor:.2f}')