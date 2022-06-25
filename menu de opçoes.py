from time import sleep

print('')
numero1 = float(input('Primeiro valor: '))
numero2 = float(input('Segundo Valor: '))
sleep(1)
print('')
print('Valores cadastrados com sucesso.')
print('')
sleep(1)
opcao = -1
while opcao != '5':
    soma = numero1 + numero2
    multiplicacao = numero1 * numero2
    print(f'Primeiro Valor: {numero1:.0f}')
    print(f'Segundo Valor: {numero2:.0f}')
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')
    opcao = str(input('>>>>> Qual é a sua opção: ')).lower().strip()
    if opcao == '1' or opcao == 'somar':
        print(f'A Soma entre {numero1:.0f} + {numero2:.0f} é {soma:.0f}')
        print('')
        sleep(2)
    elif opcao == '2' or opcao == 'multiplicar':
        print(f'O resultado de {numero1:.0f} x {numero2:.0f} é {multiplicacao:.0f}')
        print('')
        sleep(2)
    elif opcao == '3' or opcao == 'maior':
        if numero1 > numero2:
            maior = numero1
            print(f'Entre {numero1:.0f} e {numero2:.0f} o maior valor é {maior:.0f}')
        elif numero1 < numero2:
            maior = numero2
            print(f'Entre {numero1:.0f} e {numero2:.0f} o maior valor é {maior:.0f}')
        else:
            print('Os dois valores são iguais')
        print('')
        sleep(2)
    elif opcao == '4' or opcao == 'novos numeros' or opcao == 'novos números':
        print('')
        numero1 = float(input('Primeiro valor: '))
        numero2 = float(input('Segundo Valor: '))
        sleep(1)
        print('')
        print('Valores atualizados com sucesso.')
        print('')
        sleep(1)
    elif opcao == '5' or opcao == 'sair do programa':
        print('')
        print('Fim do programa.')
        print('Volte sempre.')
    else:
        print('')
        print('Opção inválida.')
        print('Escolha uma das opções abaixo:')
        print('')
        sleep(2)
