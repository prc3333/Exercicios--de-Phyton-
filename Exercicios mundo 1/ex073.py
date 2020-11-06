times = ('Flamengo', 'Atletico', 'São Paulo', 'Internacional',
         'Grêmio', 'Palmeiras', 'Sport', 'Cruzeiro', 'Botafogo',
         'Corinthias', 'Vasco da Gama', 'Fluminense', 'America-Mg',
         'Chapecoense', 'Santos', 'Vitoria', 'Bahia', 'Parana',
         'Atletico-Pr', 'Ceara')
print('=' * 23)
print(f'Lista de times do Brasileirao:{times}')
print('=' * 23)
print(f'Os cinco primeiros são:{times[0:5]}')
print('=' * 23)
print(f'Os 4 últimos são:{times[16:]}')
print('=' * 23)
print(f'Os times em ordem alfabética:{sorted(times)}')
print('=' * 23)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posicão')