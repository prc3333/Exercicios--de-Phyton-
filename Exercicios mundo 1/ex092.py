from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('carteira de trabalho (0 não tem):'))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('ano de contratação:'))
    pessoa['salário'] = float(input('salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35 - datetime.now().year)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'    -{k} tem o valor {v}')