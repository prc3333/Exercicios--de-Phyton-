n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('O Aluno está em Recuperação!!')
elif media < 5:
    print('O Aluno está Reprovado!')
elif media >= 7:
    print('O aluno está Aprovado!!!')



