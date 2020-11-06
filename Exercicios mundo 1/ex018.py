import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {}\ntem o Seno de {:.2f}\ne o Cosseno de {:.2f}\ne a Tangente e de {:.2f} '.format(ângulo, seno, cosseno, tangente))
