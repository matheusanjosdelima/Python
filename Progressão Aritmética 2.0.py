print('''
            Calculadora
       Progressão Aritmética
''')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('')
termo = 1
total_termos = 10
while termo <= total_termos:
    valor = primeiro_termo + ((termo - 1) * razao)
    print(f'{valor}', end=(" → " if termo != total_termos else ""))
    termo += 1
    if termo > total_termos:
        print('')
        total_termos += int(input('Você deseja mostrar mais quantos termos? '))
        print('')
print(f'Progressão finalizada com {total_termos} termos mostrados.')
