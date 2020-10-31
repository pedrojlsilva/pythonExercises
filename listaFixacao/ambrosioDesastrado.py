cases = int(input())
data=list()

for case in range(cases):
    line = input()
    tupla = line.split(" ")
    tuplaMod=(int(tupla[0]), tupla[1])
    data.append(tuplaMod)

data.sort(key=lambda x: x[0])
texto=str()
for case in range(cases):
    texto+=data[case][1]

print(texto)

