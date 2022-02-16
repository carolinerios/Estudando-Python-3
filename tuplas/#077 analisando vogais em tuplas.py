#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
banco_pal = ("caroline", "Historia", "Python", "curiosidade", "tecnologia", "ciencia", "analise", "dados")
print(">----"*15)
print("ANALISADOR DE PALAVRAS")
print(">----"*15)
for pal in banco_pal: # retorno cada item, neste caso, cada palavra (pal) dentro da tupla (banco_pal)
    print(f'\n A palavra "{pal}" tem as vogais: ', end = '')
    for let in pal:  # retorno cada item, neste caso, cada letra (let) dentro da string previamente retirada da tupla 
        if let.lower() in 'aeiou': #verificação item a item (letra a letra) para printar somente o que estiver na string "aeiou" 
            print(f'{let}', end = '')


