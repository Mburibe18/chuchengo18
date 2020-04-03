def mostrar_dos_listas(lista1,lista2):
    respuesta=""
    size_lista1= len(lista1)
    if (len(lista1)==len(lista2)):
        for i in range(size_lista1):
            print(i)
            print(lista1[i],lista2[i])
        respuesta ="listas mostradas con éxito"
    else: 
        respuesta="las listas no tienen la misma cantidad de elementos"
    return respuesta
