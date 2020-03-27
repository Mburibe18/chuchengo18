#-------------Mensajes------------
MENSAJE_BIENVENIDO = "Bienvenido al programa"

#-------------Codigo--------------

print(MENSAJE_BIENVENIDO)

listaAgesIniciales =[1,2,3,8,16,32,64]

def mostrar_list(listaAgesIniciales):
    if ( len ( listaAgesIniciales)):
        for i in range (len(listaAgesIniciales)):
            print (listaAgesIniciales[i])

def llenar_the_list ():
    list = []
    decision = input ("ingrese s--> para add mas ages n--> para no add mas ages : ")
    while (decision =="s"):
        list.append (input("Ingrese la age del paciente a la lista : "))
        decision = input ("ingrese s--> para add mas personas n--> para no add mas personas :")
    return list

print ("desea ingresar la age de los pacientes? : ")
ages = llenar_the_list()

mostrar_list (ages)


avarage = (((1+2+4+8+16+32+64)/7))
print ("el avarage of age is : ")
print (avarage)

listaAgesIniciales = [1,2,4,8,16,32,64]
lista_extra = [ages]
lista_extra.extend(listaAgesIniciales)
print(lista_extra)

print("la age mas grande en la lista de news {} es el {}".format(ages, max (ages)))
print("la age mas grande en la lista inicial {} es el {}".format(listaAgesIniciales, max(listaAgesIniciales)))

print("la age mas pequeña en la lista de news {} es el {}".format(ages, min(ages)))
print("la age mas pequeña en la lista inicial {} es el {}".format(listaAgesIniciales, min (listaAgesIniciales)))

ages.sort()
print("lista news ordenada creciente {}".format(ages))
listaAgesIniciales.sort()
print ("lista iniciales ordenada creciente {}".format(listaAgesIniciales))

ages.sort(reverse=True)
print ("lista news ordenada decreciente {}".format(ages))
listaAgesIniciales.sort(reverse=True)
print ("lista iniciales ordenada decreciente {}".format(listaAgesIniciales))

print(listaAgesIniciales)
listaAgesIniciales.insert (4,87)
print("you have insertado el number 87 en la position 4")
print (listaAgesIniciales)

valor_borrado = listaAgesIniciales.pop(6)
print (listaAgesIniciales , "la age deleted fue el number {} de la position seis de la lista".format(valor_borrado))