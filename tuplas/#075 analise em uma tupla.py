#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
print('Você digitará quatro valores. ')
print('-'*60)
num = (int(input('Digite um número: ')),int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))) 
print(f'Os números digitados foram: {num}')
print(f'O número 9 aparece em {num.count(9)} ocorrência(s).' if 9 in num else 'Não há ocorrência do número 9.')
print(f'O valor 3 foi digitado na {(num.index(3)+1)} posição.' if 3 in num else 'O valor 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end = '')
for n in num:
    if n%2 ==0:
        print(n,' ', end = '')
