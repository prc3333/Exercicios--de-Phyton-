distância = float(input('Qual e a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
