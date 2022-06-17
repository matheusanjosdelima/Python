from time import sleep
from random import choice

purple = '\033[35m'
red = '\033[31m'
yellow = '\033[33m'
green = '\033[32m'
clean = '\033[m'

# carregamentos
head = '''
         _______________
        |               |
        |    JOKENPÔ    |
        |_______________|
'''
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
# escolha
print(f'{purple}{head}{clean}')
escolha = str(input('Qual a sua jogada? ')).strip().lower()
# condições
if escolha in lista:
    print('')
    print('             JO', end='')
    sleep(1)
    print('KEN', end='')
    sleep(1)
    print('PÔ')
    if escolha == "pedra":
        if computador == 'pedra':
            print('    Jogador     x     Computador')
            print('     pedra               pedra  ')
            print(f'{yellow}             Empaté!!{clean}')
        elif computador == 'papel':
            print('    Jogador     x     Computador')
            print('     pedra               papel  ')
            print(f'{red}           Você perdeu!{clean}')
        else:
            print('    Jogador     x     Computador')
            print('     pedra              tesoura ')
            print(f'{green}          Você venceu!!{clean}')
    elif escolha == 'papel':
        if computador == 'papel':
            print('    Jogador     x     Computador')
            print('     papel               papel  ')
            print(f'{yellow}             Empaté!!{clean}')
        elif computador == 'tesoura':
            print('    Jogador     x     Computador')
            print('     papel              tesoura ')
            print(f'{red}           Você perdeu!{clean}')
        else:
            print('    Jogador     x     Computador')
            print('     papel               pedra  ')
            print(f'{green}          Você venceu!!{clean}')
    else:
        if computador == 'tesoura':
            print('    Jogador     x     Computador')
            print('    tesoura             tesoura ')
            print(f'{yellow}             Empaté!!{clean}')
        elif computador == 'pedra':
            print('    Jogador     x     Computador')
            print('    tesoura              pedra  ')
            print(f'{red}           Você perdeu!{clean}')
        else:
            print('    Jogador     x     Computador')
            print('    tesoura              papel  ')
            print(f'{green}          Você venceu!!{clean}')
else:
    print('Opção Inválida. Tente Novamente.')
