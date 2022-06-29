print('''
        Caixa Eletrônico
''')
valor_saque = int(input('Valor a ser sacado: R$ '))
resto = valor_saque
while resto != 0:
    notas50 = valor_saque // 50
    if notas50 > 0:
        print(f'Total de {notas50} cédula{"s" if notas50 > 1 else ""} de R$ 50,00')
    resto = valor_saque - (notas50 * 50)
    notas20 = resto // 20
    if notas20 > 0:
        print(f'Total de {notas20} cédula{"s" if notas20 > 1 else ""} de R$ 20,00')
    resto += - (notas20 * 20)
    notas10 = resto // 10
    if notas10 > 0:
        print(f'Total de {notas10} cédula{"s" if notas10 > 1 else ""} de R$ 10,00')
    resto += - (notas10 * 10)
    notas1 = resto // 1
    if notas1 > 0:
        print(f'Total de {notas1} cédula{"s" if notas1 > 1 else ""} de R$ 1,00')
    resto += - notas1
print('')
print('Volte sempre.')
