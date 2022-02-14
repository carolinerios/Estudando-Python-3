#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
prod_prec = ('Suco natural', 5.00, 'Chá', 3.40, 'Misto quente', 155.30, 'Misto quente duplo', 6.90, 'Café expresso', 5.00, 'Cappucino', 6.25, 'Omelete com tomates', 7.20, 'Omelete com queijo', 8.70)
print('-'*50)
print('LISTAGEM DE PRODUTOS')
print('-'*50)
for c in range(0, len(prod_prec)):
    if c % 2 == 0:
        print(f'{prod_prec[c]:.<50}', end = '')
    else:
        print(f'R${prod_prec[c]:.2f}')