palavras = ('aprender', 'programar', 'estudar', 'futuro')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')