#Barrio con el nombre más largo y el nombre más corto
#Los consumos mínimos y máximos para el consumo de Agua,Energía,Gas,Internet
#Cantitadad maxima de habitantes y cantidad minima de habitantes.


import pandas as pd

diccionario =pd.read_csv("datos_barrios.csv",encoding='UTF-8', header= 0,delimiter=';').to_dict()
print(diccionario["Barrio"])

mayor_nombre = max (diccionario["Barrio"].values(),key=len)
print(mayor_nombre)

menor_nombre = min (diccionario["Barrio"].values(),key=len)
print(menor_nombre)

print("\n\nla ciudad con el nombre mas largo es {} y la ciudad con el nombre mas corto es {}".format(mayor_nombre,menor_nombre))


mayor_consumo_agua = max (diccionario["Agua"].values())
print(mayor_consumo_agua)

menor_consumo_agua = min (diccionario["Agua"].values())
print(menor_consumo_agua)

print("\n\nel mayor consumo de agua fue {} y el menor consumo de agua fue {}".format(mayor_consumo_agua,menor_consumo_agua))


mayor_consumo_energia = max (diccionario["Energía"].values())
print(mayor_consumo_energia)

menor_consumo_energia = min (diccionario["Energía"].values())
print(menor_consumo_energia)

print("\n\nel mayor consumo de energia fue {} y el menor consumo de energia fue {}".format(mayor_consumo_energia,menor_consumo_energia))


mayor_consumo_gas = max (diccionario["Gas"].values())
print(mayor_consumo_gas)

menor_consumo_gas = min (diccionario["Gas"].values())
print(menor_consumo_gas)

print("\n\nel mayor consumo de gas fue {} y el menor consumo de gas fue {}".format(mayor_consumo_gas,menor_consumo_gas))


mayor_consumo_internet = max (diccionario["Internet"].values())
print(mayor_consumo_internet)

menor_consumo_internet = min (diccionario["Internet"].values())
print(menor_consumo_internet)

print("\n\nel mayor consumo de internet fue {} y el menor consumo de internet fue {}".format(mayor_consumo_internet,menor_consumo_internet))


mayor_cantidad_habitantes = max (diccionario["Habitantes"].values())
print(mayor_cantidad_habitantes)

menor_cantidad_habitantes = min (diccionario["Habitantes"].values())
print(menor_cantidad_habitantes)

print("\n\nla mayor cantidad de habitantes es {} y la menor cantidad de habitantes es {}".format(mayor_cantidad_habitantes,menor_cantidad_habitantes))