blue = '\033[34m'
red = '\033[31m'
clean = '\033[m'

print('')
frase = str(input('Escreva uma frase: ')).strip().lower()
frasefinal = str("".join(frase.split()))
frasecontagem = int(len(frasefinal))
inversa = ''
for c in range(frasecontagem - 1, -1, -1):
    inversa = inversa + frasefinal[c]
if inversa == frasefinal:
    print(f'''
A Frase {blue}{frase.title()}{clean} é um {red}palíndromo{clean}!!!
Não sabe o que é?? Deixa que eu te explico.

{red}Palíndromo{clean} é uma palavra, frase ou número
que permanece igual quando lida de trás
para frente.

Muito legal né??''')
else:
    print(f'''
Pena que essa frase não é um {red}palíndromo{clean}.''')
