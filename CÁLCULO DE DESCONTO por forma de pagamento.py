green = '\033[32m'
red = '\033[31m'
clean = '\033[m'

print('')
preco = float(input('Qual o preço do produto? '))
pagamento = str(input('Qual a forma de pagamento? ')).strip()
vezes = 1
if 'dinheiro' in pagamento.lower() or 'cheque' in pagamento.lower():
    valor = preco - (preco * 0.1)
elif 'credito' in pagamento.lower() or 'crédito' in pagamento.lower():
    vezes = int(input('Em quantas vezes? '))
    if vezes == 1:
        valor = preco - (preco * 0.05)
    elif vezes == 2:
        valor = preco
    elif vezes >= 3:
        valor = preco + (preco * 0.2)
    else:
        valor = 'INVÁLIDO'
elif 'debito' in pagamento.lower() or 'débito' in pagamento.lower():
    valor = preco - (preco * 0.05)
elif pagamento.lower() == 'cartao' or pagamento.lower() == 'cartão':
    cartao = str(input('Débito ou Crédito: '))
    if 'credito' in cartao.lower() or 'crédito' in cartao.lower():
        vezes = int(input('Em quantas vezes? '))
        if vezes == 1:
            valor = preco - (preco * 0.05)
        elif vezes == 2:
            valor = preco
        elif vezes >= 3:
            valor = preco + (preco * 0.2)
        else:
            valor = 'INVÁLIDO'
    elif 'debito' in cartao.lower() or 'débito' in cartao.lower():
        valor = preco - (preco * 0.05)
    else:
        valor = 'INVÁLIDO'
else:
    valor = 'INVÁLIDO'
print('')
print(f'O valor total ficou {green}R$ {valor:.2f}{clean}, em {red}{vezes}{clean}'
      f' {f"vez" if vezes == 1 else f"vezes"} de {red}R$ {valor / vezes:.2f}{clean}')
