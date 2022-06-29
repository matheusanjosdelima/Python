from random import randint
from random import choice
from time import sleep

lista = ['PAR', 'ÍMPAR']
vitorias = 0
inicial1 = choice(lista)
if inicial1 == 'PAR':
    inicial2 = 'ÍMPAR'
else:
    inicial2 = 'PAR'
inicial_numero1 = randint(0, 5)
inicial_numero2 = randint(0, 5)
print(f'''
      {inicial1}''', end='      ')
sleep(0.5)
print(inicial2)
sleep(1)
print(f'        {inicial_numero1}        {inicial_numero2}')
sleep(0.5)
if (inicial_numero1 + inicial_numero2) % 2 == 0:
    if inicial_numero2 == 'PAR':
        print('              ', end='')
    else:
        print('     ', end='')
else:
    if inicial_numero2 == 'ÍMPAR':
        print('              ', end='')
    else:
        print('     ', end='')
print('GANHEI!!')
sleep(1)
print('')
print('Agora é sua vez!! Faça sua escolha')
while True:
    escolha = str(input('PAR ou ÍMPAR: ')).strip().upper()
    while escolha != 'PAR' and escolha != 'ÍMPAR':
        print('')
        print('Escolha Inválida')
        print('Tente Novamente')
        print('')
        escolha = str(input('PAR ou ÍMPAR: ')).strip().upper()
    if escolha == 'PAR':
        print('eu escolho ÍMPAR')
    else:
        print('eu escolho PAR')
    print('')
    numero = int(input('Agora escolha um número de 0 à 5: '))
    computador = randint(0, 5)
    while not 5 >= numero >= 0:
        print('')
        print('Escolha Inválida')
        print('Tente Novamente')
        print('')
        numero = int(input('Agora escolha um número de 0 à 5: '))
    print(f'Computador: {computador}')
    if (numero + computador) % 2 == 0:
        if escolha == 'PAR':
            vitorias += 1
            print('')
            print('Parabéns você ganhou!!')
            print('')
        else:
            if vitorias == 0:
                print('')
                nova_tentativa = str(input('Que pena você não conseguiu ganhar nenhuma vez. Que tal tentar '
                                           'de novo? [ S/N ] ')).strip().lower()
                print('')
                while nova_tentativa != 'sim' and nova_tentativa != 's' and nova_tentativa != 'não' and \
                        nova_tentativa != 'n':
                    print('')
                    print('Escolha Inválida')
                    print('Tente Novamente')
                    print('')
                if nova_tentativa == 'não' or nova_tentativa == 'nao':
                    break
            elif vitorias == 1:
                print('')
                nova_tentativa = str(input('Que pena você só ganhou uma vez seguida de mim. Que tal uma melhor '
                                           'de três? [ S/N ] ')).strip().lower()
                print('')
                while nova_tentativa != 'sim' and nova_tentativa != 's' and nova_tentativa != 'não' and \
                        nova_tentativa != 'n':
                    print('')
                    print('Escolha Inválida')
                    print('Tente Novamente')
                    print('')
                if nova_tentativa == 'não' or nova_tentativa == 'nao':
                    break
                else:
                    vitorias = 0
            else:
                print('Nessa eu ganhei')
                sleep(1)
                print(f'Parabéns você ganhou {vitorias} vezes seguidas de mim.')
                break
    else:
        if escolha == 'ÍMPAR':
            vitorias += 1
            print('')
            print('Parábens você ganhou!!')
            print('')
        else:
            if vitorias == 0:
                print('')
                nova_tentativa = str(input('Que pena você não conseguiu ganhar nenhuma vez. Que tal tentar '
                                           'de novo? [ S/N ] ')).strip().lower()
                print('')
                while nova_tentativa != 'sim' and nova_tentativa != 's' and nova_tentativa != 'não' and \
                        nova_tentativa != 'n':
                    print('')
                    print('Escolha Inválida')
                    print('Tente Novamente')
                    print('')
                if nova_tentativa == 'não' or nova_tentativa == 'nao':
                    break
            elif vitorias == 1:
                print('')
                nova_tentativa = str(input('Que pena você só ganhou uma vez seguida de mim. Que tal uma melhor '
                                           'de três? [ S/N ] ')).strip().lower()
                print('')
                while nova_tentativa != 'sim' and nova_tentativa != 's' and nova_tentativa != 'não' and \
                        nova_tentativa != 'n':
                    print('')
                    print('Escolha Inválida')
                    print('Tente Novamente')
                    print('')
                if nova_tentativa == 'não' or nova_tentativa == 'nao':
                    break
                else:
                    vitorias = 0
            else:
                print('Nessa eu ganhei')
                sleep(1)
                print(f'Parabéns você ganhou {vitorias} vezes seguidas de mim.')
                break
