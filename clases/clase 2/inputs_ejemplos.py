
PREGUNTA_NOMBRE ="ingrese su nombre"
MENSAJE_BIENVENIDO ="bienvenido"
MENSAJE_ENTRADA ="a este programa"
PREGUNTA_EDAD ="ingrese su edad: "
MENSAJE_EDAD ="tu edad es"
PREGUNTA_ESTATURA ="ingrese su estatura: "
MENSAJE_ESTATURA ="tu estatura es"
MENSAJE_DESPEDIDA ="chau"

_nombrePersona = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDO,_nombrePersona, MENSAJE_ENTRADA)
_edadPersona =int(input(PREGUNTA_EDAD))
print(MENSAJE_EDAD,_edadPersona,)
print (type(_edadPersona))
_estaturaPersona =float(input(PREGUNTA_ESTATURA))
print(MENSAJE_ESTATURA,_estaturaPersona,)
print (type(_estaturaPersona))
print (MENSAJE_DESPEDIDA)
