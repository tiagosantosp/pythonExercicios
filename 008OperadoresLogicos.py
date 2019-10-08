None
# é considerado como nada

not True
#not ele inverto o valor sendo assim retornaria false

a = True
b = False

a and b
# Para o operador AND precisamos que os dois valores sejam
# verdadeiros caso contrario ele retorna false

a or b
# Para o Operador OR se apenas um dos argumentos for
# verdadeiro ele retorna True caso os dois sejam falsos
# ele vai retornar False

#Temos tambem os operadores para comparar o valor

c = 10
d = 20

c > d
# C é maior que D
#FALSE

c < d
# C é menor que D
#TRUE

c >= d
# C é maior ou igual que D
#FALSE

c <= d
# C é menor ou igual que D
#TRUE

c == d
# C é igual que D
#FALSE

c != d
# C é diferente que D
#TRUE


#podemos comparar STRINGS tambem

curso = "Aula de Python"

"python" in curso
# estamos perguntando se a palavra PYTHON esta
# dentro da variavel curso
# TRUE

"python" not in curso
# estamos perguntando se a palavra PYTHON não esta
# dentro da variavel curso
# FALSE
