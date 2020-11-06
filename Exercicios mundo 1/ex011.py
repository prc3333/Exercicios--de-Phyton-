alt = float(input('altura da parede: '))
lag = float(input('Largura da parede:'))
area = alt * lag
print(' Sua parede tem a dimensão de {}x{} e sua area e de {}m²'.format(alt, lag, area))
tinta = area / 2
print('Para pintar essa parede,você precisará de {}L de tinta.'.format(tinta))
