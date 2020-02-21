#------------Mensajes--------------
MENSAJE_BIENVENIDO ="bienvenido"
MENSAJE_DESPEDIDA = "chau crack"
PREGUNTA_ESTATURA ="ingrese su estatura: "
PREGUNTA_NOMBRE ="ingrese su nombre : "
PREGUNTA_ESTATURA ="ingrese su estatura: "
PREGUNTA_PESO = "ingrese su peso "
MENSAJE_BAJO_PESO ="estas muy flaco"
MENSAJE_SALUDABLE = "estas en forma"
MENSAJE_SOBREPESO = "tienes que bajar unos kilitos"
MENSAJE_OBESIDAD_MORBIDA ="tienes que bajar muchos kilos"
MENSAJE_TOCAYO ="somos tocayos obesos morbidos"
#------------Variables--------------
NOMBRE_PERSONAL ="Marco"
IMC = 0.0
#------------Entradas-----------------
_nombreUsuario = " "
_pesoUsuario = 0
_estaturaUsuario = 0
#-------------Codigo---------------------
print(MENSAJE_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
_pesoUsuario = float (input (PREGUNTA_PESO))
_estaturaUsuario = float (input (PREGUNTA_ESTATURA))
IMC = (_pesoUsuario/_estaturaUsuario**2)
print (IMC)
if (IMC >= 12) and (IMC <= 18) :
 print(MENSAJE_BAJO_PESO)
elif (IMC >= 19) and (IMC <= 24) :
    print(MENSAJE_SALUDABLE)
elif (IMC >= 30) and (IMC <= 39) :
    print(MENSAJE_SOBREPESO)
else:
    print(MENSAJE_OBESIDAD_MORBIDA)
    print(MENSAJE_TOCAYO)
print(MENSAJE_DESPEDIDA)
