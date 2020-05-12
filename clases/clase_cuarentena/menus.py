MENSAJE_WELCOME = "hola , khe onda"
PREGUNTA_AGE = "Dime tu age"
PREGUNTA_LIST_DE_COMPRAS = "do you like to adquirir articulos ? s ->si n ->no "
listCompras = "this will be tu lista de compras product by product"
deleteProducto = "do u like to delete  un product de la lista ? cual ? s ->si n->no"
PREGUNTA_NUMBER = "ingresa el number de products que quieras eliminar"

print(MENSAJE_WELCOME)

_desicion = int (input("""
    enter :
    1-age
    2-lista de productos to buy
    3-lista de compras product by product
    4-delete un product de la lista de compras
    5-salir
"""))

while (_desicion != 5):
    if(_desicion ==1):
        _ageUsuario = int(input(PREGUNTA_AGE))
        if  ((_ageUsuario >= 0) and (_ageUsuario <= 17)) :
            print("income denied")
        elif((_ageUsuario >= 18) and (_ageUsuario <= 29)):
             print("adelante , pase pss")
        elif (_ageUsuario >=30) and (_ageUsuario <=59):
            print("wow ,you have un discount del 30%")
        else:
            print("wow,you have un discount igualito a tu edad")
    elif (_desicion ==2) :
        products = []
        _listCompras = input(PREGUNTA_LIST_DE_COMPRAS)
        #TE FALTABA DOBLE IGUAL QUE SE EMPLEA PARA PREGUNTAR
        while (_listCompras =="s") :
            products.append (input("ingrese :"))
            _listCompras = input (PREGUNTA_LIST_DE_COMPRAS)
        print (products)


    else:
        print("ingrese un valor que sea valido")
    _desicion = int (input("""
      ingrese :
      1-age
      2-lista de productos to buy
    3-lista de compras product by product
    4-delete un product de la lista de compras
    5-salir
"""))
print("gracias por la confianza wey")