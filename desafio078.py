valores = list()
print('')
for contagem in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('')
print(f'Você digitou os valores:', end=' ')
print(*valores, sep=', ')
quant_posicoes_max = valores.count(max(valores))
if quant_posicoes_max > 1:
    posicao = -1
    posicoes_max = list()
    for posicao_inicial in range(0, quant_posicoes_max):
        posicao = valores.index(max(valores), posicao + 1)
        if posicao not in posicoes_max:
            posicoes_max.append(posicao)
    print(f'O maior valor foi {max(valores)} nas posições:', end=' ')
    print(*posicoes_max, sep=', ')
else:
    print(f'O maior valor foi {max(valores)} na posição: {valores.index(max(valores))}')
quant_posicoes_min = valores.count(min(valores))
if quant_posicoes_min > 1:
    posicao = -1
    posicoes_min = list()
    for posicao_inicial in range(0, quant_posicoes_min):
        posicao = valores.index(min(valores), posicao + 1)
        if posicao not in posicoes_min:
            posicoes_min.append(posicao)
    print(f'O menor valor foi {min(valores)} nas posições:', end=' ')
    print(*posicoes_min, sep=', ')
else:
    print(f'O menor valor foi {min(valores)} na posição: {valores.index(min(valores))}')
