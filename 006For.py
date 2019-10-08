#loop com For
#repete um bloco de código

#temos diversas maneiras de montar o loop

# podemos passar uma tupla
#for i in [1,2,3]:

#podemos passar uma string
#for i in 'novo loop':

#podemos utilizar o método range
#o primeiro número representa início
#o segundo número representa o fim
#o terceiro o salto
for i in range(0,20,2):
   print(i)
#Else será executado no final do loop
else:
    print('fim')
   
lista1 = ('maça','banana','limão')
lista2 = ['laranja','jaca','melão']

#o zip percorre duas listas juntas
for i,j in zip(lista1, lista2):
    print(i,j)
    
#temos também o enumerate que mostra o índice da lista
for i,j in enumerate(lista1):
    print(i,j)
   
 