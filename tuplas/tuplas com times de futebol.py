#Criar uma tupla prenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
#A - Os 5 primeiros, B - Os últimos, C- Times em ordem alfabética, D- Em que posição está o Chapecoense

times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense'
print('Os primeiros colocados são: ')
for p in range(0,4):
    print(times[p]) # formatar com if c < 4: ', ' else: '.'
print (f'Os quatro últimos colocados são: {times[-4:]} ')
print(f'Os times do Brasileirão em ordem alfabética: {sorted(times)}')
pos = len
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}')