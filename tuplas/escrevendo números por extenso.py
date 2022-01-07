# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

acabou = False #definindo condição para laço
enc = ' '
num_ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while not acabou:
    num = int(input('Digite um número entre 0-20 para vê-lo escrito por extenso: '))
    while num > 21 or num < 0:
        if num > 21:
            print('Você digitou um número maior que 20')
            num = int(input('Digite um número entre 0-20 para vê-lo escrito por extenso: '))
        if num < 0:
            print('Você digitou um número menor que o')
            num = int(input('Digite um número entre 0-20 para vê-lo escrito por extenso: '))
    esc = num_ext[num] # extraindo a posição específica da tupla
    print(f'O número {num} por extenso é {esc}')
    while enc not in 'SN':
        enc = str(input('Você deseja ver mais números por extenso? Responda S/N' )).strip().upper()
    if enc == 'S':
        enc = ' '
    else:
        acabou = True
print('='*20)
print('FIM')