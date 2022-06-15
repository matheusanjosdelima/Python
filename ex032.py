from datetime import date
verde = '\033[32m'
vermelho = '\033[31m'
sublinhado = '\033[4m'
negrito = '\033[1m'
limpa = '\033[m'

ano = int(input(f'{negrito}Que ano quer analisar?{limpa} Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {verde}{ano}{limpa} é {negrito}{sublinhado}bissexto{limpa}')
else:
    print(f'O ano {verde}{ano}{limpa} não é {negrito}{sublinhado}bissexto{limpa}')
