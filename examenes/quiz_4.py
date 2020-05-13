import matplotlib.pyplot as plt
import pandas as p

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Unidades", fontsize =20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Unidade")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(14,20)
plt.savefig("ElementovsUnidades.png")
plt.close()

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Viejo", fontsize =20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Viejo")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(14,20)
plt.savefig("ElementovsViejo.png")
plt.close()

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Nuevos", fontsize =20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Nuevos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(14,20)
plt.savefig("ElementovsNuevos.png")
plt.close()

ppg=p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x=list(ppg["muestra"].values())
y=list(ppg["valor"].values())
plt.title("Ppg del paciente")
plt.xlabel("Tiempo(milisegundos)")
plt.ylabel("Voltaje(microVoltios)")
plt.plot(x,y)
plt.savefig("Ppg.png")
plt.show()

print("Veo nueve picos")

labels= 'Casa','Hospitalizado','UCI'
sizes =[85,10,5]
explode =[0, 0, 0.5]
plt.pie(sizes, explode=explode, labels=labels, shadow=True , startangle=0)
plt.title("Lugares de Recuperacion")
plt.savefig("Recuperacion_en_Colombia.png")
plt.show()