class Canguros():
    def __init__(self,identificacion,edad):
        self.identificacion = identificacion
        self.edad = edad
    def saltos(self,numero_saltos,):
        for i in range(numero_saltos):
            print ("salto", i+1)



class Cuidadores():
    def __init__(self,nombre,identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    def cantidad_canguros(self,alimentar):
        print("he alimentado tal cantidad de canguros")
        





class Jefes(Cuidadores):

    def contratar_cuidadores_nuevos(self,nombre,identificacion):
        print("procedo a contratarlos")



    def dar_mensaje (self,mensaje):
        print("dare un mensaje en nombre de todos")


canguro1 = Canguros(123,2)
canguro2 = Canguros(433,6)
canguro3 = Canguros(544,2)
canguro4 = Canguros(990,3)
canguro5 = Canguros(655,8)
canguro6 = Canguros(766,1)
canguro7 = Canguros(312,7)
canguro8 = Canguros(444,4)
canguro9 = Canguros(565,10)
canguro10 = Canguros(999,5)

canguro1.saltos(43)
canguro2.saltos(43) 
canguro3.saltos(43)
canguro4.saltos(43)
canguro5.saltos(43)
canguro6.saltos(43)
canguro7.saltos(43)
canguro8.saltos(43)
canguro9.saltos(43)
canguro10.saltos(43)      

cuidador1 = Cuidadores("Jaime",123)
cuidador2 = Cuidadores("Nuria",345)
cuidador3 = Cuidadores("Paula",567)
cuidador4 = Cuidadores("Sebastian",368)
cuidador5 = Cuidadores("teacher",111)

cuidador1.cantidad_canguros(2)
cuidador2.cantidad_canguros(6)
cuidador3.cantidad_canguros(9)
cuidador4.cantidad_canguros(7)
cuidador5.cantidad_canguros(16)

jefe1 = Jefes("Marco",100)
jefe1.contratar_cuidadores_nuevos("Tomas",223)
jefe1.dar_mensaje("hello everyone")


