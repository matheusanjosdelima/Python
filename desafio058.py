from random import randint

print('''
            Você consegue
              adivinhar?
''')
print('''Vou pensar em um número de 0 a 10
será que você consegue advinhar?
''')
computador = randint(0, 10)
tentativas = 1
numero_jogador = int(input('Escolha um número: '))
while numero_jogador != computador:
    if 0 <= numero_jogador <= 10:
        print('Desculpe mas você ainda não acertou.')
        print('Tente novamente!')
        numero_jogador = int(input('Escolha um número: '))
        tentativas += 1
    else:
        print('Você sabe que eu pensei em um número de 0 a 10 certo?')
        print('Tente novamente!')
        numero_jogador = int(input('Escolha um número: '))
print('')
print(f'Você acertou na {tentativas}ª tentativa!!!\n'
      f'O número que eu pensei foi o {computador}')
