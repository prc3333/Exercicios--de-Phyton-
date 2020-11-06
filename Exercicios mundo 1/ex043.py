peso = float(input('Qual é o seu peso?(Kg) '))
altura = float(input('Qual é a sua altura?(m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso Normal!')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
elif imc >= 40:
    print('Você está em OBesidade Morbida, Cuidado!')
