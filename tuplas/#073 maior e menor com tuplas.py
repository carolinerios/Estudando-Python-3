#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
c = 0
num_ale =(randint(1,50),randint(1,50), randint(1,50), randint(1,50), randint(1,50)) #criando a tupla com números aleatorios
print(f'Os números aleatorizados são: ',end='')
for n in num_ale: 
    c = c+1
    print(n,', 'if c != len(num_ale) else '.', end ='') # formatar o uso de vírgula ou ponto final
print(f'\n O maior número sorteado é: {sorted(num_ale)[-1]} \n E o menor número é: {sorted(num_ale)[0]}') #fatiamento da tupla, buscando pela primeira e última posição