# umaNovaEsperanca = {'princesa':'leia', 'han':'solo'}
# oDespertar = umaNovaEsperanca
# oDespertar['kylo']='ren'
# print(oDespertar)
# print(umaNovaEsperanca)

# exemplo1 = {'orfao1':'violet', 'orfao2':'klaus', 'orfao3':'sunny'}
# exemplo2 = {'orfao2':'klaus', 'orfao1':'violet', 'orfao3':'sunny'}

# if(exemplo1==exemplo2):
#     print("hey boudelaire")

# exemplo3=['duncan', 'isadora', 'quigley']
# exemplo4=['isadora', 'duncan', 'quigley']
# if(exemplo3==exemplo4):
#     print("hey quag")


pokedex = {"agua": {"squirtle":{"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"jato agua"},
                    "magikarp": {"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"esguicho"}},
          "pedra":{"onix":{"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"triturar"}},
           "fogo":{"charizard":{"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"flamejante"}},
       "eletrico":{"pikachu":{"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"choque do trocao"},
                        "electabuzz": {"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"relampago"}},
       "fantasma": {"haunter": {"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"garra"}},
        "psiquico": {"abra":{"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"choque psiquico"}} }

# for chave in pokedex:
#     print(chave[0])

def todos(pokedex:dict)->list:
    pokemonsConhecidos=[]
    for tipo in pokedex:
        for pokemon in pokedex[tipo]:
            pokemonsConhecidos.append([pokemon, tipo])
    return pokemonsConhecidos

print(todos(pokedex))

# pokedex["pedra"]["geodude"] = {"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"investida"}
# print(pokedex["pedra"])
# novaCat="fada"
# pokedex[novaCat]["jigglypuff"] = {"pontos de vida":60, "ataque": 30, "defesa": 10, "golpe":"cantar"}
# print(pokedex["fada"])



