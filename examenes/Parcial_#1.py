MENSAJE_BIENVENIDA ="hola, bienvenid@"
print (MENSAJE_BIENVENIDA)


class Estudiante ():
    def __init__(self, nombre, edad, genero, colegio_de_procedencia):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.colegio = colegio_de_procedencia
    def clases(self, numero_de_clases):
        for i in range (numero_de_clases):
            print ("hola , soy un estudiante que se llama {} , tengo {} años , soy del genero {} y vengo del colegio {} y  he asistido a {} clases , mucho gusto".format(self.nombre ,self.edad,self.genero,self.colegio,i+1 ))


class Profesor ():
    def __init__(self,nombre,edad,nivel_educativo):
        self.nombre = nombre
        self.edad = edad
        self.nivel_educativo =  nivel_educativo
    def dictar_clases(self, numero_de_clases_dictadas):
        for i in range (numero_de_clases_dictadas):
            print("hola, soy un profesor que se llama {} , tengo {} años , mi nivel educativo es {} , y he dictado {} el dia de hoy , un placer".format(self.nombre , self.edad , self.nivel_educativo , i+1))


class Directores(Profesor):
    def contratar_profesores(self,nombre,edad,nivel_educativo):
        print("procedo a contratar al profesor {} , de edad {} y con un nivel educativo de {}".format(self.nombre,self.edad,self.nivel_educativo))
        profesor = Profesor(nombre,edad,nivel_educativo)
        return profesor


estudiante1 = Estudiante("Marco",19,"masculino","ccb")
estudiante1.clases(13)

estudiante2 = Estudiante("Isabella",19,"femenino","theodoro")
estudiante2.clases(32)

estudiante3 = Estudiante("Andres",18,"masculino","ccb")
estudiante3.clases(22)

estudiante4 = Estudiante("Tomas",18,"masculino","ccb")
estudiante4.clases(7)

estudiante5 = Estudiante("Angie",17,"femenino","cumbres")
estudiante5.clases(12)

docente1 = Profesor("Juan",27,"doctorado")
docente1.dictar_clases(16)

docente2 = Profesor("Daniel",28,"master en programacion")
docente2.dictar_clases(17)

rector = Directores("Julian",44,"doctorado superior")
rector.contratar_profesores("Javier",33,"titulo universitario")

docente3 = rector.contratar_profesores("Samue",34,"bachiller")
docente3.dictar_clases(32)

docente4 = rector.contratar_profesores("Luara",44,"bachiller")
docente4.dictar_clases(23)


_desicion = int (input("""
    enter :
    1. Mostrar los atributos de los estudiantes s
    2. Mostrar los atributos de los profesores
    3. Mostrar los atributos del director
    4. Salir
    """))

while (_desicion != 4):
        if (_desicion ==1):
            print(estudiante1.nombre,estudiante1.edad,estudiante1.genero,estudiante1.colegio,estudiante2.nombre,estudiante2.edad,estudiante2.genero,estudiante2.colegio,estudiante3.nombre,estudiante3.edad,estudiante3.genero,estudiante3.colegio,
            estudiante4.nombre,estudiante4.edad,estudiante4.genero,estudiante4.colegio,estudiante5.nombre,estudiante5.edad,estudiante5.genero,estudiante5.colegio)
        elif (_desicion ==2):
            print(docente1.nombre,docente1.edad,docente1.nivel_educativo,docente2.nombre,docente2.edad,docente2.nivel_educativo,docente3.nombre,docente3.edad,docente3.nivel_educativo,docente4.nombre,docente4.edad,docente4.nivel_educativo)
        elif (_desicion ==3):
            print(rector.nombre,rector.edad,rector.nivel_educativo)
        else :
            print("ingrese un valor valido")

        _decision = int (input("""
      ingrese :
      1. Mostrar los atributos de los estudiantes s
      2. Mostrar los atributos de los profesores
      3. Mostrar los atributos del director
      4. Salir
      """))
print("gracias por usarme")   


