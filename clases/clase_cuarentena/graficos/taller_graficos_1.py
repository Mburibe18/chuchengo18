
import matplotlib.pyplot as plt
import pandas as p

barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Barrios vs Agua", fontsize =20)
plt.bar(barrios["Barrio"].values(),barrios["Agua"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(14,20)
plt.savefig("BarriosvsAgua.png")
plt.close()


barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Barrios vs Gas",fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Gas"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Gas")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(14,20)
plt.savefig("BarriosvsGas.png")
plt.close()

ecg=p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x=list(ecg["muestra"].values())
y=list(ecg["valor"].values())
plt.title("Ecg (microVoltios) del paciente")
plt.xlabel("Tiempo(milisegundos)")
plt.ylabel("Voltaje(microVoltios)")
plt.plot(x,y)
plt.savefig("Ecg.png")
plt.show()

labels= 'Bogota','Medellin','Leticia','Villavicencio'
sizes =[80,70,5,8]
explode =[0, 0, 0.4, 0]
plt.pie(sizes, explode=explode, labels=labels, shadow=True , startangle=0)
plt.title("Porcentaje de contagiados")
plt.savefig("Contagiados_en_Colombia.png")
plt.show()