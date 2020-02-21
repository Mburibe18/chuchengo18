PREGUNTA_NOMBRE ="ingrese su nombre : "
MENSAJE_BIENVENIDO ="bienvenido"
MENSAJE_ENTRADA ="a este programa"
PREGUNTA_EDAD ="ingrese su edad: "
MENSAJE_EDAD ="tu edad es"
PREGUNTA_ESTATURA ="ingrese su estatura: "
MENSAJE_ESTATURA ="tu estatura es"
MENSAJE_TOCAYO = "Hola nene como vas"
MENSAJE_DESPEDIDA = "chau crack"
MENSAJE_JOVEN = "eres joven y beio"
MENSAJE_ADULTO = "eres adulto"
MENSAJE_ADULTO_MAYOR = "estas arrugado"
#--------------VARIABLES------------
NOMBRE_PERSONAL = "Marco"
#----------------ENTRADAS----------------------
_nombreUsuario = " "
_edadUsuario = 0
#----------------CODIGO------------------------
print(MENSAJE_BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL== _nombreUsuario) :
    print(MENSAJE_TOCAYO)
_edadUsuario = int (input(PREGUNTA_EDAD))

if (_edadUsuario >= 0) and (_edadUsuario <= 25) :
    print(MENSAJE_JOVEN)
elif (_edadUsuario >= 26) and (_edadUsuario <= 65) :
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_ADULTO_MAYOR)
print(MENSAJE_DESPEDIDA)