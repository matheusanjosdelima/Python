purple = '\033[35m'
red = '\033[31m'
bold = '\033[1m'
clean = '\033[m'

print('')
print(f'{purple}{bold}{"Todos os números pares":^31}{clean}')
print(f'{red}{bold}{"Entre 1 e 50":^31}{clean}')
print('')
for c in range(2, 51, 2):
    print(f'{c:2}', end='   ')
    if c % 7 == 0:
        print('')
print('')
