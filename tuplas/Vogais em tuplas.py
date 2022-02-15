#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
banco_pal = ("caroline", "Historia", "Python", "curiosidade", "tecnologia", "ciencia", "analise", "dados")
print("><  "*33)
print("ANALISADOR DE PALAVRAS")
for pal in banco_pal: #
    print(f'\n A palavra "{pal}" tem as vogais: ', end = '')
    for let in pal:
        if let.lower() in 'aeiou':
            print(f'{let}', end = '')


