print('')
numero = int(input('Digite um número inteiro: '))
fatorial = 1
print('')
if numero > 1:
    print(f'{numero}! = {numero}', end='')
    for termos in range(numero - 1, 0, -1):
        fatorial *= termos
        print(f' * {termos}', end='')
    print(f' = {fatorial * numero}')
elif numero == 1:
    print('1! = 1')
elif numero == 0:
    print('0! = 1')
else:
    print('Não existe fatorial de números negativos.')
