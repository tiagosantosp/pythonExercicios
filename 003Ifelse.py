#a estrutura do if é muito simples
#coloca if condição :
#no python o bloco do if é a indentação
a = 1
b = 2

#vamos testar o maior valor
#se o teste der verdadeiro executa o 
#primeiro bloco
if a > b:
    print('a é maior')
#se não executa esse
elif b > a:
    print('b é maior')
#caso todos os testes de errado
#executa esse
else:
    print('iguais')
