#para trabalhar erros utilize o try
try:
    #aqui você coloca o que ele vai tentar fazer
    1/0
#coloque uma excessão e o tipo de erro
# e uma variavel para receber o erro
except(BaseException)as erro:
    print(erro)
#se não conseguir tratar o erro
else:
    print('se não')
#após terminar o processo
finally:
    print('erro tratado')
    