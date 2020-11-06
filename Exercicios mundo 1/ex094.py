from random import randint
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador4': randint(1, 6),
        'jogador5': randint(1, 6),
        'jogador6': randint(1, 6)}
print(jogo)
for k, v in jogo.items():
    print(f' => 0 {k} tirou {v}')
