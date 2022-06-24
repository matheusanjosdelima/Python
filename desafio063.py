print('')
numero = int(input('Digite a quantidade de termos da Sequência de Fibonacci: '))
penultimo = 0
ultimo = 0
valor = 1
termos = 2
if numero >= 1:
    print(penultimo, end=' ')
    while termos <= numero:
        print(valor, end=' ')
        penultimo = ultimo
        ultimo = valor
        valor = penultimo + ultimo
        termos += 1
else:
    print('Valor inválido.')
