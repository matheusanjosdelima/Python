print('''
            Cálculo da Média''')
termo = 0
soma = 0
maior = 0
menor = 0
continuar = 's'
while continuar == 's' or continuar == 'sim':
    print('')
    valor = float(input('Digite um número: '))
    soma += valor
    termo += 1
    if termo == 1:
        maior = menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    continuar = str(input('Deseja continuar? ')).strip().lower()
    while continuar != 'n' and continuar != 'não' and continuar != 'nao' and continuar != 's' and continuar != 'sim':
        print('Desculpe, não entendi. Digite novamente.')
        continuar = str(input('Deseja continuar? ')).strip().lower()
print('')
print(f'A media {f"dos {termo} números digitados foi" if termo > 1 else "do número é"} {soma / termo:.1f}, sendo que\n'
      f'O maior número foi {maior:.0f} e o menor foi {menor:.0f}.')
