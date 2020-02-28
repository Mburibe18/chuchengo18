#---------------MENSAJE---------
MENSAJE_BIENVENIDO ="bienvenido"
MENSAJE_DESPEDIDA = "chau crack"
MENSAJE_ESTADO_SALUDABLE = "estas bien"
MENSAJE_ESTADO_HIPOTERMIA = "tienes frio"
MENSAJE_ESTADO_DE_ALERTA = "cuidado , estas enfermo"
MENSAJE_ESTADO_DE_PELIGRO = "estas hirviendo wey"
PREGUNTA_PAIS_PACIENTE = "ingrese su pais de procedencia : " 
MENSAJE_ESTADO_OBSERVACION = "ur under observation"
PREGUNTA_TEMPERATURA_PACIENTE ="ingrese temperatura del paciente"

#--------------VARIABLES-------------
NOMBRE_PERSONAL ="Marco"

#--------------ENTRADA---------------
_temperaturaPaciente = 0.0
_paisPaciente = ""

#--------------CODIGO----------------
print(MENSAJE_BIENVENIDO)
_paisPaciente =  input (PREGUNTA_PAIS_PACIENTE)
if (_paisPaciente == "china") or (_paisPaciente == "iran") or (_paisPaciente == "italia") :
    print (MENSAJE_ESTADO_OBSERVACION)
_temperaturaPaciente = float (input(PREGUNTA_TEMPERATURA_PACIENTE))
if (_temperaturaPaciente >= 36) and (_temperaturaPaciente <= 38.4) :
    print (MENSAJE_ESTADO_SALUDABLE)
elif (_temperaturaPaciente <= 36) :
    print (MENSAJE_ESTADO_HIPOTERMIA)
elif (_temperaturaPaciente >= 38.5) and (_temperaturaPaciente <= 40) :
    print (MENSAJE_ESTADO_DE_ALERTA)
else:
    print (MENSAJE_ESTADO_DE_PELIGRO)
print (MENSAJE_DESPEDIDA)            
