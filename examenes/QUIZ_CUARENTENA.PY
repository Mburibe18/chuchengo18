MENSAJE_DE_BIENVENIDA = "Hola , bienvenid@"
print(MENSAJE_DE_BIENVENIDA)


_desicion = int(input("""
    ingrese:
    1. para ver peso y la presion de cada paciente
    2.para añadir el peso de los pacientes
    3.datos de las presiones 
    4.para terminar
"""))

while(_desicion !=4):
    if(_desicion ==1):
        def mostrar_dos_listas (lista_numero_1 , lista_numero_2):
            if (len (lista_numero_1) == len (lista_numero_2)):
                print ("peso" , "presion")
                for i in range (len(lista_numero_1)):
                    print (lista_numero_1[i], lista_numero_2[i])

pesoPacientes =[32,64,74,85,94,115,122,127,137,148]
presionesPacientes =[presion_1,presion_2,presion_3,presion_4,presion_5,
presion_6,presion_7,presion_8,presion_9,presion_10]

        presion_1 = (32*6)
        presion_2 = (64*6)
        presion_3 = (74*6)
        presion_4 = (85*6)
        presion_5 = (98*6)
        presion_6 = (115*6)
        presion_7 = (122*6)
        presion_8 = (127*6)
        presion_9 = (137*6)
        presion_10 = (148*6)

        print (presion_1,presion_2,presion_3,presion_4,presion_5,presion_6,presion_7,presion_8,
        presion_9,presion_10)


        mostrar_dos_listas = (pesoPacientes,presionesPacientes)



    elif (_desicion =2)
        def muestre_la_lista (lista_numero_1)
            if (len(lista_numero_1))
                print ("esta es la lista de los pesos de los pacientes")
                for i in range (len(lista_numero_1))
                    print (lista_numero_1[i])


        def llenarLista ():
            lista = []
            desicion = input ("ingresa s -->para agregar mas pesos n--> para no agregar mas pesos :")  
            while (desicion == "s"):
                lista.append("ingresa s -->para agregar mas pesos n--> para no agregar mas pesos :")
                return lista
        
        print("desea ingresar el peso de los pacientes? :")
        pesos= llenarLista()

        mostrar_lista (pesos)


    elif (_desicion ==3):
        print("la presion mas alta en la lista de pacientes nuevos {} es el {}".format(presionesPacientes,max(presionesPacientes)))
        print("la presion mas baja en la lista de pacientes nuevos {} es el {}".format(presionesPacientes,min(presionesPacientes)))

        presionesPacientes.sort(reverse=True)
        print("lista de presiones de manera decreciente {}".format(presionesPacientes))
        print("este es el numero de pacientes ingresados")
        
        print(len(pesoPacientes))

else:
    print("ingrese un numero valido")

_desicion= int(input("""
 ingrese :
 1.para ver peso y la presion de cada paciente
 2.para añadir el peso de los pacientes
 3.datos de las presiones 
 4.para terminar
"""))
print("gracias por la confianza")    