'''listnum = []
for c in range(0, 5):
    listnum.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'você digitou os valores {listnum}')
print(f'O maior valor digitado foi:{max(listnum)}')
print(f'O menor valor digitado foi:{min(listnum)}')'''

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor numerico {c+1}: ')))
print(f'Minha lista é {lista}.')
print(f'O menor numero é {min(lista)} na posição {lista.index(min(lista))}')
print(f'O maior  numero é {max(lista)} na posição {lista.index(max(lista))}')
