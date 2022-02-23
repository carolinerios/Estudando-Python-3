#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lis_num = []
menor = 0
maior = 0
pos_mai = []
pos_men = []
print('-'*15)
print('ANALISADOR DE MAIOR E MENOR')
print('-'*15)
print('Você digitará 5 valores')
for c in range(0,5):
    lis_num.append(int(input(f"Digite um número para posição {c}: ")))
    if c == 0:
        menor = maior = lis_num[0]
    else:
        if lis_num[c] < menor:
            menor = lis_num[c]
        if lis_num[c] > maior:
            maior = lis_num[c]
for i, v in enumerate(lis_num):
    if v == menor:
        pos_men.append(i)
    if v == maior:
        pos_mai.append(i)
print(lis_num)
print(f'O maior valor digitado foi {maior} na posição {pos_mai} e o menor foi {menor} na posição {pos_men}')