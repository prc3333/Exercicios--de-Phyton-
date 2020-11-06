print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO:
[1] à vista Dinheiro/cheque
[2] à vista no Cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual e a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço *5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} sem Juros!'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de {:.2f} com Juros!'.format(totparc, parcela))
else:
    total = preço
    print('Opção Inválida de pagamento Tente novamente!')
print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, total))
