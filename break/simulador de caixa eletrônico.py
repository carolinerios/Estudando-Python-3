'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''
soma = cinq = vint = dez = um = 0
dinh = int(input('Quando deseja sacar? R$ '))
while True:
    while dinh > 50 or dinh == 50:
        dinh = dinh - 50
        cinq = cinq + 1
    while dinh > 20 or dinh == 20:
        dinh = dinh - 20
        vint = vint + 1
    while dinh > 10 or dinh == 10:
        dinh = dinh - 10
        dez = dez+1
    while dinh > 1 or dinh == 1:
        dinh = dinh - 1
        um = um+1
    if soma == 0:
        break
if cinq > 0:
    print(f'Você receberá {cinq} de R$50')
if vint > 0:
    print(f'Você receberá {vint} de R$20')
if dez > 0:
    print(f'Você receberá {dez} de R$10')
if um > 0:
    print(f'Você receberá {um} de R$1')