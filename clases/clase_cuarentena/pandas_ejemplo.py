#Cual es la ciudad con el nombre más largo?
#Cual es la ciudad con el nombre más corto?
#Cual fue el mayor monto de ganancias? 
#Cual fue el mayor monto de perdidas? 

import pandas as pd

diccionario =pd.read_csv("balance.csv",encoding='UTF-8',header = 0,delimiter=';').to_dict()
print(diccionario["Ciudad"])

mayor_nombre = max (diccionario["Ciudad"].values(),key=len)
print(mayor_nombre)

menor_nombre = min (diccionario["Ciudad"].values(),key=len)
print(menor_nombre)

print("\n\nla ciudad con el nombre mas largo es {} y la ciudad con el nombre mas corto es {}".format(mayor_nombre,menor_nombre))


mayor_monto_ganancias = max(diccionario["Ganancias"].values())
mayor_monto_perdidas = max(diccionario["Perdidas"].values())
print(mayor_monto_ganancias)
print(mayor_monto_perdidas)

print("\n\nel mayor monto de perdidas fue {} y el menor monto de perdidad fue {}".format(mayor_monto_ganancias,mayor_monto_perdidas))
