

class Estoque:
    def __init__(self):
        self.estoque=[]
    def insert(self, codigo, quantidade):
        self.estoque.append([codigo, quantidade])

    def venda(self, codigo, quantidade):
        for produto in self.estoque:
            if produto[0]==codigo and quantidade <= produto[1]:
                produto[1]-=quantidade
                print('OK')

            elif produto[0]==codigo and quantidade > produto[1]:
                print('ESTOQUE INSUFICIENTE')


    def printRelatorio(self):
        for produto in self.estoque:
            print(str(produto[0]) + " " + str(produto[1]))



estoque=Estoque()

line = list(map(int, input().split(' ')))

while line[0] != 9999:
    estoque.insert(line[0],line[1])
    line = list(map(int, input().split(' ')))


line = list(map(int, input().split(' ')))
while line[0] != 9999:
    estoque.venda(line[1],line[2])
    line = list(map(int, input().split(' ')))

estoque.printRelatorio()
