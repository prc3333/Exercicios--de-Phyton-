real = float(input('Quanto dinheiro você possui?R$'))
dolar = real / 3.7074
e = real / 4.36
print('Com R${} voce pode comprar US${:.2f}'.format(real, dolar))
print('Com R${} voce pode comprar E{:.2f}'.format(real, e))