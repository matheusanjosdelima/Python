from random import randint

sorteados = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior = menor = sorteados[1]
print(f'''
Os valores sorteados foram:''', end=' ')
for numero in sorteados:
    print(numero, end=' ')
print(f'''
O maior valor sorteado foi {max(sorteados)}
O menor valor sorteado foi {min(sorteados)}''')
