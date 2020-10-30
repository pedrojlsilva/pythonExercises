line=input()
apostadores=[]
resultados=[]

# inserindo novos apostadores
while line != 'FIM':
    newLine=line.split(" ")
    for apostador in apostadores:
        if newLine[0]==apostador[0]:
            apostadores.remove(apostador)

    apostadores.append(newLine)
    line=input()

line=input()
newLine=line.split("-")
resultados=list(newLine)

acertos=[]
# contando os acertos de cada apostador
for apostador in apostadores:
    count = 0
    for resultado in resultados:
        for i in range (1,len(apostador)):
            if resultado == apostador[i]:
                count+=1

    acertos.append([apostador[0], count])


acertos.sort(key=lambda x: (x[1], x[0]))

for acerto in acertos:
    plusSignal = "+" * int(acerto[1])
    print(acerto[0] + " "+plusSignal)
