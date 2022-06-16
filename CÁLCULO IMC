red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
underline = '\033[4m'
bold = '\033[1m'
clean = '\033[m'

print('')
peso = float(input(f'Qual o seu {underline}peso(kg){clean}? '))
altura = float(input(f'Qual a sua {underline}altura(m){clean}? '))
imc = peso / (altura ** 2)
if imc <= 0:
    imc = 'Inválido'
print('')
print(f'O IMC dessa pessoa é de {green if 18.5 <= imc < 25 else red}{imc:.1f}{clean}')
if imc < 18.5:
    condicao = f'{yellow}abaixo do peso{clean}'
elif imc < 25:
    condicao = f'em seu {green}peso ideal{clean}'
elif imc < 30:
    condicao = f'em {yellow}sobrepeso{clean}'
elif imc < 40:
    condicao = f'em {red}obesidade{clean}'
else:
    condicao = f'em {red}{bold}obesidade mórbida{clean}'
print(f'Ela está {condicao}.')
