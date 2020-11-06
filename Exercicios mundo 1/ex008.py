#m = float(input('digite o seu valor em metros: '))
#c = m * 100
#mm = m * 1000
#print('O seu valor em metros digitado foi de: {} e o seu valor convertidor em  centimentros e:{}'.format(m,c))
#print('O seu valor convertidor em milimitros e:{}'.format(mm))
met = float(input('Uma distancia em metro: '))
km = met / 1000
hm = met / 100
dam = met / 10
dm = met * 10
cm = met * 100
mm = met * 1000
print('A sua medida em metros foi de:{}\ne o valor em Km e de:{}\ne o valor em Hm e de:{}\ne o valor em dam e de:{}'.format(met, km, hm,dam))
print('e o valor em dm e de:{}\neo valor em cm e de:{}\neo valor em mm e de:{}'.format(dm, cm, mm))