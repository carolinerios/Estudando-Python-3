som_pre = c_prod = c = 0
while True:
    nom_prod =  str(input('Qual o produto o comprado? '))
    pre_prod = float(input('Qual o preço do produto comprado? '))
    som_pre = pre_prod + som_pre
    c = c+1
    if pre_prod >1000:
        c_prod = c_prod + 1
    if c == 1 or pre_prod < barato:
        barato = pre_prod 
        menor = nom_prod
    end = str(input('Encerrar compra? Digite S/N ')).strip().upper()[0]
    if end in 'S':
        break
print(f'A soma da compra foi de R$ {som_pre}')
print(f'{c_prod} produto(s) comprado(s) custa(m) mais de R$1.000')
print(f'O produto mais barato foi {menor}')