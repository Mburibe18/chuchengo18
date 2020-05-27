import sys
#--------------------------------------------------------------#

import matplotlib.pyplot as plt
import pandas as p


def validador_de_archivo (file):
    assert(file)
    return False
validador = True

while (validador):
    file =  input('ingrese el nombre del archivo : ')
    try:
        validador = open (file)
        validador = False
    except FileNotFoundError:
        print("La entrada no es válida")


ppg = p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("ingrese el nombre del eje x : "))
plt.ylabel(input("ingrese el nombre del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()


#--------------------------------------------------------------#
nombre = "No ingresaste el nombre"
try:
    nombre = (input('Ingrese su nombre : '))
except ValueError:
    print ("ingresaste mal el nombre")
print ("Hola", nombre)

edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad : '))
except ValueError:
    print ("ingresaste mal la edad")
print ("Su edad es", edad)

estatura = "No ingresaste tu estatura"
try:
    estatura = float (input('Ingrese su estatura : '))
except ValueError:
    print ("ingresaste mal la estatura")
print ("Tu estatura es", estatura)

peso = "No ingresaste tu peso"
try:
    peso = float (input('Ingrese su peso : '))
except ValueError:
    print ("ingresaste mal el peso")
print ("Tu peso es", peso)

IMC = ((peso/estatura**2))
print ("Tu imc es de  : ",IMC)

#--------------------------------------------------------------#
ppg = p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("ingrese el nombre del eje x : "))
plt.ylabel(input("ingrese el nombre del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()

print("hay 9 crestas")

ecg = p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("ingrese el nombre del eje x : "))
plt.ylabel(input("ingrese el nombre del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()

print("hay 9 crestas")

eeg = p.read_csv("eeg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(eeg["muestra"].values())
y = list(eeg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("ingrese el nombre del eje x : "))
plt.ylabel(input("ingrese el nombre del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()

print ("hay 10 crestas")


topes = {
    "Nombres_archivos" : ["ppg","ecg","eeg"],
    "Crestas_archivos" : [9,9,10]
}

plt.bar(topes["Nombres_archivos"],topes["Crestas_archivos"])
plt.title("Comparaciones en numeros de crestas")
plt.xlabel("Nombres_archivos")
plt.ylabel("Crestas_archivos")
plt.savefig(input("Comparacion_numero_crestas.png"))
plt.show()

#------------------------------------------------------------#
labels = 'Cuarto', 'Sala', 'Cocina','Garage','Balcon','Baño'
sizes = [65, 5, 5, 5, 5, 15 ]
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("% DE TIEMPO EN ESPACIOS DE LA CASA")
plt.savefig("Grafica_de_casa.png")
plt.show()

#-----------------------------------------------------------#
print("La diferencia esta en que en el aprendizaje supervisado , una persona nunca se dara cuenta si en realidad adquirio dicho conocimiento o no , mientras que en el no supervisado , la persona se enfrenta a los problemas por si misma , unicamente defendiendose con los conocimientos adquiridos")
