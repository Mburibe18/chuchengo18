class Persona ():
    #Cada vez que cree un humano
     def __init__(self ,nombre, talla,sexualidad,peso,edad):
       self.raza = "Ser humano"
       self.name = nombre
       self.size = talla
       self.gender = sexualidad
       self.weight = peso
       self.age = edad
       print ("Hola a todos soy un", self.raza, "minombre es",self.name)

     def mostrar_atributos(self):
         print("mi nombre es ",self.name)
         print("mi estatura es",self.size)
         print("mi genero es",self.gender)
         print("mi peso es",self.weight)
         print("mi edad es",self.age)

     def caminar(self,cantidad_pasos):
         for i in range (cantidad_pasos):
             print("he caminado",i+1,"pasos")

ser_humano_1 = Persona("Marco",1.83,"masculino",70,19)

ser_humano_1.caminar(100)
