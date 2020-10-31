dados=list()


passagem=int(input())

while passagem != -1:
    date=input()
    saida=input()
    destino=input()
    horario=input()
    poltrona=int(input())
    idade=int(input())
    nome=input()
    dados.append((nome, poltrona, idade))

    passagem=int(input())

idadeMedia=0
for passageiro in dados:
    idadeMedia+=passageiro[2]

idadeMedia=idadeMedia/(len(dados))

for passageiro in range(dados):
    if passageiro[2] > idadeMedia and (passageiro[1] % 2 ==0):
        print(passageiro.nome)
