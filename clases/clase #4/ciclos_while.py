# numero = 0
# NUMERO_DESEADO = 12
# while (NUMERO_DESEADO >= numero):
#     numero = numero +1
#     print (numero)
# print (numero)    

import random 
PREGUNTA_NUMERO = """ingrese un numero 
entero 
entre 1 - 10
:"""
NUMERO_FAVORITO = random.randint(1,10)
MENSAJE_FALLO = "QUE TORTA"
MENSAJE_ACIERTO = "QUE PRO WEY"
MENSAJE_MAYOR = "ESTAS CERCA"
MENSAJE_MENOR = "ESTAS LEJOS"

_numeroIngresado = int(input(PREGUNTA_NUMERO))
while (NUMERO_FAVORITO != _numeroIngresado):
    print (MENSAJE_FALLO)
    if (_numeroIngresado > NUMERO_FAVORITO):
        print (MENSAJE_MAYOR)
    else: print (MENSAJE_MENOR)
    _numeroIngresado = int(input(PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)
