while True:
    t = int(input('Quer ver a tabuada de qual valor?'))
    if t < 0:
        break
    print('-' * 32)
    for c in range(1, 11):
        print(f'{t} x {c:2} = {t*c}')
print('Programa Tabuada Encerrado.Volte Sempre!')
