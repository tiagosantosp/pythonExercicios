#loop com while
#repete tudo que estiver dentro do bloco


#precisamos de uma variável de controle
i = 0

#enquanto i maior que 10 ele faz
while i < 10:
    if i == 5:
        #continue volta para 
        i += 1
        continue
    elif i == 8:
        #break finaliza o while
        break
    else:
        print(i)
    i += 1