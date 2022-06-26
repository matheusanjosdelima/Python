print('''
            Calculadora
       Progressão Aritmética
''')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('')
termo = 0
total_termos = 10
while total_termos > termo:
    termo += 1
    valor = primeiro_termo + ((termo - 1) * razao)
    print(f'{valor}', end=(" → " if total_termos > termo else ""))
    if total_termos == termo:
        print('')
        total_termos += int(input('Você deseja mostrar mais quantos termos? '))
        print('')
print(f'Progressão finalizada com {termo} termos mostrados.')
