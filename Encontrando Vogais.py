lista_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
                  'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
print('')
for palavra in lista_palavras:
    print(f'Na palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print('')
