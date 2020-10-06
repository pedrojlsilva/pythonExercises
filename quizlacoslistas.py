# numeros = [[1,2,3], [4,5,6], [7,8,9]]
# print(numeros[2][0])

# pedpaptes=["pedra","papel", "tesoura"]
# print(pedpaptes[3])

# print(pedpaptes[0])


def calcPeri(lados:list[int]) -> int:
    soma:int=0
    for lado in lados:
        soma+= lado

    return soma

print(calcPeri([12,12,24,42]))

# nome = "joana"

# for i in nome:
#     if i=="a":
#         print("oi j")