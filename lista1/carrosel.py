numberOfValues=int(input())
carrossel = list(map(int, input().split(' ')[:numberOfValues]))

# Carrossel-> Array circular
carrosselDuplo=[]
for veiculo in carrossel:
    carrosselDuplo.append(veiculo)

for veiculo in carrossel:
    carrosselDuplo.append(veiculo)

countMax=0

for i in range(0, len(carrosselDuplo)):
    count=1
    for j in range(i+1,len(carrosselDuplo)):
        if carrosselDuplo[j]>carrosselDuplo[j-1]:
            count+=1
        else:
            break

    if count>countMax:
        countMax=count


print(countMax)
