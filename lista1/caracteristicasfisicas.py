idade=int(input())
maisVelho=0
countPessoas=0
mulheres=0
while idade != -1:
    countPessoas+=1
    sexo, cabelo, cor = input().split(" ")
    if idade>maisVelho:
        maisVelho=idade
    
    if sexo == "f" and cabelo == "l" and cor=="v" and idade>=18 and idade<=35:
        mulheres+=1

    idade=int(input())

print("Mais velho: " + str(maisVelho))
resultado=(mulheres*100)/countPessoas
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: {:.2f}%".format(resultado))
