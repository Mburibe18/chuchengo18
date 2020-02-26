#--------------MENSAJES--------------
MENSAJE_BIENVENIDO ="bienvenido"
MENSAJE_DESPEDIDA = "chau crack"
PREGUNTA_PACIENTES = "ingrese numero de pacientes"
MENSAJE_RIESGO_BAJO = "esta en riesgo medio"
MENSAJE_RIESGO_MEDIO = "esta en riesgo medio"
MENSAJE_RIESGO_ALTO = "esta en riesgo alto"
MENSAJE_UCI = "esta en riesgo alto"
#--------------VARIABLES-------------
NOMBRE_PERSONAL ="Marco"
PREGUNTA_UCI = "ingrese numero de pacientes en uci"
#--------------ENTRADA---------------
_numeroPacientes= 0
_numeroPacientesuci= 0
#--------------CODIGO----------------
print(MENSAJE_BIENVENIDO)
_numeroPacientes = int (input (PREGUNTA_PACIENTES))
if (_numeroPacientes > 0) and (_numeroPacientes < 1000) :
 print (MENSAJE_RIESGO_BAJO)
elif (_numeroPacientes > 1000) and (_numeroPacientes <=5000) :
    _numeroPacientesuci = int (input(PREGUNTA_UCI))
    if (_numeroPacientes >=1000):
        print(MENSAJE_UCI)
    else:
        print (MENSAJE_RIESGO_MEDIO)
else:
    print(MENSAJE_RIESGO_ALTO)
