from random import randint

ganhador = 0
vitorias = 0

print('')
print('-=' * 29)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^56}')
print('-=' * 29)
while True:
    valor = int(input('Digite um valor de 0 à 5: '))
    while not 0 <= valor <= 5:
        print('')
        print('Valor Inválido. Tente novamente.')
        print('')
        valor = int(input('Digite um valor de 1 à 5: '))
    computador = randint(0, 5)
    soma = valor + computador
    opcao = str(input('Par ou ímpar: ')).strip(). upper()
    while opcao != 'PAR' and opcao != 'ÍMPAR' and opcao != 'IMPAR':
        print('')
        print('Opção Inválida. Tente novamente.')
        print('')
        opcao = str(input('Par ou ímpar: ')).strip().upper()
    print('-' * 56)
    print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}:', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
        if opcao == 'PAR':
            print('Você VENCEU!')
            print('Vamos Jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!')
            print('-=' * 29)
            print(f'GAME OVER!', end=' ')
            if vitorias == 0:
                print('Você não ganhou nenhuma vez.')
                tentar_de_novo = str(input('Quer tentar de novo? [ S/N ] ')).strip().lower()
                while tentar_de_novo != 'sim' and tentar_de_novo != 's' and tentar_de_novo != 'não' \
                        and tentar_de_novo != 'nao' and tentar_de_novo != 'n':
                    print('')
                    print('Desculpe, não entendi. Tente novamente.')
                    print('')
                    tentar_de_novo = str(input('Quer tentar de novo? [ S/N ] ')).strip().lower()
                if tentar_de_novo == 's' or tentar_de_novo == 'sim':
                    vitorias = 0
                else:
                    break
            else:
                print(f'Você venceu {vitorias} {"vez" if vitorias == 1 else "vezes"}')
                break

    else:
        print('DEU ÍMPAR')
        if opcao == 'IMPAR' or opcao == 'ÍMPAR':
            print('Você VENCEU!')
            print('Vamos Jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!')
            print('-=' * 29)
            print(f'GAME OVER!', end=' ')
            if vitorias == 0:
                print('Você não ganhou nenhuma vez.')
                tentar_de_novo = str(input('Quer tentar de novo? [ S/N ] ')).strip().lower()
                while tentar_de_novo != 'sim' and tentar_de_novo != 's' and tentar_de_novo != 'não' \
                        and tentar_de_novo != 'nao' and tentar_de_novo != 'n':
                    print('')
                    print('Desculpe, não entendi. Tente novamente.')
                    print('')
                    tentar_de_novo = str(input('Quer tentar de novo? [ S/N ] ')).strip().lower()
                if tentar_de_novo == 's' or tentar_de_novo == 'sim':
                    vitorias = 0
                else:
                    break
            else:
                print(f'Você venceu {vitorias} {"vez" if vitorias == 1 else "vezes"}')
                break
    print('-' * 56)
