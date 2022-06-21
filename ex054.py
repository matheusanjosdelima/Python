from datetime import date

red = '\033[31m'
purple = '\033[35m'
blue = '\033[34m'
clean = '\033[m'

maior = 0
menor = 0

print('')
for c in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if date.today().year - ano_nascimento > 21:
        maior += 1
    else:
        menor += 1
print('')
print('Nesse grupo temos,', end=' ')
if maior > 0:
    print(f'{purple}{maior} {"pessoa maior" if maior == 1 else "pessoas maiores"}{clean} de idade', end='')
    if menor > 0:
        print(' e', end=' ')
    else:
        print('.')
if menor > 0:
    print(f'{blue}{menor} {"pessoa menor" if menor == 1 else "pessoas menores"}{clean} de idade.')
