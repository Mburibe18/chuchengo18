#-------------Mensajes------------
MENSAJE_BIENVENIDO = "Bienvenido al programa"

#-------------Codigo--------------

print(MENSAJE_BIENVENIDO)

listaEdadesIniciales =[1,2,3,8,16,32,64]

def mostrar_lista(listaEdadesIniciales):
    if ( len ( listaEdadesIniciales)):
        for i in range (len(listaEdadesIniciales)):
            print (listaEdadesIniciales[i])

def llenar_lista ():
    lista = []
    decision = input ("ingrese s--> para agregar mas edades n--> para no agregar mas edades : ")
    while (decision =="s"):
        lista.append (input("Ingrese la edad del paciente a la lista : "))
        decision = input ("ingrese s--> para agregar mas personas n--> para no agregar mas personas :")
    return lista

print ("desea ingresar la edad de los pacientes? : ")
edades = llenar_lista()

mostrar_lista(edades)


promedio = (((1+2+4+8+16+32+64)/7))
print ("este es promedio de edad : ")
print (promedio)

listaEdadesIniciales = [1,2,4,8,16,32,64]
lista_extra = [edades]
lista_extra.extend(listaEdadesIniciales)
print(lista_extra)

print("la edad mas grande en la lista de nuevos {} es el {}".format(edades, max (edades)))
print("la edad mas grande en la lista inicial {} es el {}".format(listaEdadesIniciales, max(listaEdadesIniciales)))

print("la edad mas pequeña en la lista de nuevos {} es el {}".format(edades, min(edades)))
print("la edad mas pequeña en la lista inicial {} es el {}".format(listaEdadesIniciales, min (listaEdadesIniciales)))

edades.sort()
print("lista nuevos ordenada creciente {}".format(edades))
listaEdadesIniciales.sort()
print ("lista iniciales ordenada creciente {}".format(listaEdadesIniciales))

edades.sort(reverse=True)
print ("lista nuevos ordenada decreciente {}".format(edades))
listaEdadesIniciales.sort(reverse=True)
print ("lista iniciales ordenada decreciente {}".format(listaEdadesIniciales))

print(listaEdadesIniciales)
listaEdadesIniciales.insert (4,87)
print("tu has insertado el numero 87 en la posicion 4")
print (listaEdadesIniciales)

valor_borrado = listaEdadesIniciales.pop(6)
print (listaEdadesIniciales , "la edad borrada fue el numero {} de la posicion seis de la lista".format(valor_borrado))