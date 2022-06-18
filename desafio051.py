purple = '\033[35m'
underline = '\033[4m'
clean = '\033[m'

print(f'''{purple}

       Progressão Aritmética

{clean}''')
termo1 = float(input(f'Digite o {underline}primeiro{clean} {underline}termo{clean} da {purple}PA{clean}: '))
razao = float(input(f'Digite a {underline}razão{clean}: '))
print('')
for c in range(1, 11):
    print(f'{termo1 + ((c - 1 ) * razao):3.0f}', end='     ')
    if c % 5 == 0:
        print('')
