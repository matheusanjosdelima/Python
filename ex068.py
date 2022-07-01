from random import randint

ganhador = 0
vitorias = 0

print('')
print('-=' * 29)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^56}')
print('-=' * 29)
while True:
    valor = int(input('Digite um valor de 1 à 5: '))
    while not 0 < valor <= 5:
        print('')
        print('Valor Inválido. Tente novamente.')
        print('')
        valor = int(input('Digite um valor de 1 à 5: '))
    computador = randint(1, 5)
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
        ganhador = 'PAR'
    else:
        print('DEU ÍMPAR')
        ganhador = 0
    print('-' * 56)
    if opcao == ganhador:
        print('Você VENCEU!')
        print('Vamos Jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
print('-=' * 29)
print(f'GAME OVER! Você venceu {vitorias} {"vez" if vitorias == 1 else "vezes"}')