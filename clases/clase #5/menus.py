
listaNombres = ["Santiago",
                   "juanes",
                   "marco",
                   "elena",
                   "mch betancur",
                   "mch mesa",
                   "leslly",
                   "ysabella",
                   "santiago el mejor",
                   "daniel",
                   "mafer",
                   "david",
                   "susana",
                   "teacher"]
listaEdades =[18 ,
              19 ,
              20 , 
              21 , 
              22 ,
              23 ,
              24 ,
              25 ,
              26 ,
              27 ,
              28 ,
              29 ,
              30 ,
              31 ]

listaNotas = [3.0 ,
               2.5 ,
               4.9 ,
               3.4 ,
               5.0 ,
               3.4 ,
               3.8 ,
               4.0 ,
               2.0 ,
               3.5 ,
               5.0 ,
               3.2 ,
               1.2 ,
               4.4 ,
               4.3 ]     
listaNombres[4]= "mch betancur"
listaNombres[5]= "mch mesa"
print(listaNombres)
listaNombres.pop(13)
print(listaNombres)
listaNombres.append("teacher")
print(listaNombres)

#---------CODIGO----------
_desicion = int (input("""
    ingrese :
    1-para ver lista de Nombres
    2-para ver edades
    3-para ver notas
    4-salir
"""))
while (_desicion !=4):
    if (_desicion ==1):
        print(listaNombres)
    elif (_desicion ==2) :
        print(listaEdades)
    elif (_desicion ==3):
        print(listaNotas)
    else:
        print ("ingrese un valor valido")
    _desicion = int (input("""
        ingrese :
        1-para ver lista de nombres
        2-para ver edades
        3-para ver notas
        4-salir
    """))
print ("gracias por usar el programa")  

#---------CODIGO--------

