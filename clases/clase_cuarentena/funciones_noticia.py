import funciones_lectura as helper
noticia= "Noticia.txt"
lineas=helper.leer_archivo(noticia)
helper.mostrar_lineas(lineas)
Texto = ["Es verdad que esta pandemia nos afecta a todos\n" , "pero" , "a pesar de todo" , "tenemos que sobrellevar esta\n" "situacion de la mejor manera posible y buscar una solucion." "Una posible\n" "solucion podria ser como decia el presidente es jugar el torneo a puertas cerradas" , "tambien \n" "tanto directivos como jugadores podrian rebajar su salario" , "que sea un % mutuo." "tambien se podria\n" "vender la mercancia a un menor precio" , "pero buscar alternativas para que\n" "el equipo de nuestros amores no caiga mas bajo."]
helper.agregar_lineas_archivo("noticia.txt","\nPeriodico el Colombiano" "\n   18 de Abril")


