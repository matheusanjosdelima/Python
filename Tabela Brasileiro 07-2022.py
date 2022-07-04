from time import sleep

cor = ''
clean = '\033[m'
tabela_brasileirao = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 'Fluminense',
                      'São Paulo', 'Flamengo', 'Santos', 'Botafogo', 'Avaí', 'Coritiba', 'America-MG', 'Bragantino',
                      'Ceara', 'Atletico-GO', 'Goias', 'Cuiaba', 'Juventude', 'Fortaleza')
tabela_brasileirao_ordem = sorted(tabela_brasileirao)
print('')
print('Lista de Times do Brasileirão: ')
sleep(0.5)
print('')
for c in range(0, len(tabela_brasileirao)):
    if c < 5:
        cor = '\033[32m'
    elif c > 15:
        cor = '\033[31m'
    else:
        cor = ''
    print(f'{c + 1:2}  {cor}{tabela_brasileirao[c]}{clean}')
    sleep(0.5)
print('')
print('Lista dos Times em Ordem Alfabética: ')
sleep(0.5)
print('')
for c in range(0, len(tabela_brasileirao)):
    print(f'{tabela_brasileirao_ordem[c]}')
    sleep(0.5)
print('')
print(f'O Corinthias está na {tabela_brasileirao.index("Corinthians") + 1}ª posição.')
