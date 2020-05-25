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


ecg = p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title(input("ingrese el titulo de la grafica : "))
plt.xlabel(input("ingrese el nombre del eje x : "))
plt.ylabel(input("ingrese el nombre del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como desea guardar la grafica : "))
plt.show()

#-----------------------------------------------------------------#

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


#------------------------------------------------------------------#


kilogramos_arroz= "No ingresaste los kilogramos de arroz"
try:
    kilogramos_arroz = float (input('Ingrese los kilogramos de arroz : '))
except ValueError:
    print ("ingresaste mal los kilogramos de arroz")
print ("los kilogramos de arroz que compraste fueron", kilogramos_arroz)

kilogramos_lentejas = "No ingresaste los kilogramos  de lentejas"
try:
    kilogramos_lentejas = float (input('Ingrese los kilogramos de lentejas : '))
except ValueError:
    print ("ingresaste mal los kilogramos de lentejas")
print ("los kilogramos  de lentejas que compraste fueron", kilogramos_lentejas)

kilogramos_frijoles = "No ingresaste los kilogramos de frijoles"
try:
    kilogramos_frijoles = float (input('Ingrese los kilogramos de frijoles : '))
except ValueError:
    print ("ingresaste mal los kilogramos de frijoles")
print ("los kilogramos de frijoles que compraste fueron", kilogramos_frijoles)

kilos_papa = "No ingresaste los kilogramos de papa"
try:
    kilogramos_papa = float (input('Ingrese los kilogramos de papa : '))
except ValueError:
    print ("ingresaste mal los kilogramos de papa")
print ("los kilogramos de papa que compraste fueron", kilogramos_papa)

mercado = {
    "articulos" : ["Arroz", "Lentejas", "Frijoles", "Papa"]
}
kilogramos = (kilogramos_arroz, kilogramos_lentejas, kilogramos_frijoles, kilogramos_papa)


print (mercado["articulos"])
print (kilogramos)

plt.bar (mercado["articulos"], kilogramos)
plt.title("articulos vs Kilogramos", fontsize=25)
plt.xlabel("(articultos)")
plt.ylabel("(kilogramos)")
plt.savefig("articulososVskilogramos.png")
plt.show ()
#------------------------------------------------------------------#
def validador_opinion (opinion):
    assert(opinion.endswith("."))
    return False
validador = True

while (validador):
    opinion =  input('En esta cuarentena me he dado cuenta de que hay que valorar todo lo que tenemos : ')
    try:
        validador = validador_opinion (opinion)
    except AssertionError:
        print("La entrada no es válida")

#---------------------------------------------------------------------#
labels = 'Leche', 'Huevo', 'Vino','Arroz','Queso','Salchichas'
sizes = [12, 8, 4, 26, 30, 20]
explode = (0, 0, 0, 0, 0.2, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("% DE COMPRAS")
plt.savefig("Grafica_de_compras.png")
plt.show()












































































