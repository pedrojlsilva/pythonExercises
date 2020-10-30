numberCases = int(input())


for i in range(numberCases):
    primeiraPassada=""
    segundaPassada=""
    terceiraPassada=""
    newString = input()
    for j in newString:
        if j.isalpha():
            primeiraPassada+=chr(ord(j)+3)
        else:
            primeiraPassada+=j

    segundaPassada = primeiraPassada[::-1]


    metade=int(len(segundaPassada)/2)


    terceiraPassada = segundaPassada[0:metade]
    for j in range(metade,len(segundaPassada)):
        terceiraPassada+=chr(ord(segundaPassada[j])-1)

    print(terceiraPassada)
    



