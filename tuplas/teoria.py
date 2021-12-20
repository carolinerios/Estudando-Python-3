lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}') #mostrando cada item da tupla

for cont in range (0, len([lanche])):
    print(cont) # mostrar a numeração 

for cont in range (0, len(lanche)):
    print(lanche[cont]) #mostrando o item da tupla que está nas posições do contador. lanche no contador 1 é hamburguer...

for pos, comida in enumerate(lanche): #se eu precisar mostrar a ordem dos itens na tupla, eu posso usar o enumerate
    print(f'Eu vou comer {comida} na posição {pos}') 

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # a ordem influencia
print(c) # me retorna todos os itens, em ordem
print(len(c)) # contar o total de itens
print(c.index(5)) #para saber a posição do 5 
print(c.count(5)) #para contar quantos números 5 aparecem
print(c.index(5,1) # o ultimo numero seleciona a partir de que ponto eu quero que a contagem inicie)
del(c) #não podemos mudar a tupla, mas podemos deletá-la