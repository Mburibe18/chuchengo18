#--------MENSAJES------
MENSAJE_BIENVENIDO = "hola , khe onda"
#--------CODIGO--------
PREGUNTA_EDAD = "Dime tu age"
#--------CODIGO--------
PREGUNTA_LISTA_DE_COMPRAS = "deseas adquirir articulos ? s ->si n ->no "
#--------CODIGO--------
listaCompras = "this will be tu lista de compras producto a producto"
#--------CODIGO--------
eliminarProducto = "do u like to delete  un producto de la lista ? cual ? s ->si n->no"
#--------CODIGO--------
PREGUNTA_NUMERO = "ingresa el number de products que quieras eliminar"
#---------------------------------
print(MENSAJE_BIENVENIDO)

_desicion = int (input("""
    ingrese :
    1-age
    2-lista de productos to buy
    3-lista de compras producto a producto
    4-delete un producto de la lista de compras
    5-salir
"""))

while (_desicion != 5):
    if(_desicion ==1):
        _edadUsuario = int(input(PREGUNTA_EDAD))
        if  ((_edadUsuario >= 0) and (_edadUsuario <= 17)) :
            print("income denied")
        elif((_edadUsuario >= 18) and (_edadUsuario <= 29)):
             print("adelante , pase pss")
        elif (_edadUsuario >=30) and (_edadUsuario <=59):
            print("obtienes un discount del 30%")
        else:
            print("obtienes un discount igualito a tu edad")
    elif (_desicion ==2) :
        productos = []
        _listaCompras = input(PREGUNTA_LISTA_DE_COMPRAS)
        #TE FALTABA DOBLE IGUAL QUE SE EMPLEA PARA PREGUNTAR
        while (_listaCompras =="s") :
            productos.append (input("ingrese :"))
            _listaCompras = input (PREGUNTA_LISTA_DE_COMPRAS)
        print (productos)


    else:
        print("ingrese un valor que sea valido")
    _desicion = int (input("""
      ingrese :
      1-age
      2-lista de productos to buy
    3-lista de compras producto a producto
    4-delete un producto de la lista de compras
    5-salir
"""))
print("gracias por la confianza wey")