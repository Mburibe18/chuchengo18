#-----------MESSAGE-------
WELCOME_MESSAJE="Hi mate , welcome to this program"

#------------CODE-------


print(WELCOME_MESSAJE)

weightInitialpatients =[32,64,74,85,98,115,122,127,137,148]


def show_list(weightInitialpatients):
    if (len(weightInitialpatients)):
        for i in range (len(weightInitialpatients)):
            print(weightInitialpatients[i])

show_list(weightInitialpatients)
preasures= []
for weight in weightInitialpatients:
    preasures.append(weight*6)

def complete_list (listainicial):
    patientPreasure = []
   
    decition =  input("""
    enter :
        1. to see patient weight and preasure
        2. to add patient new weight
        3. to see the higher preasure
        4. to see the lower preasure
        5. to know the total number of patients
        6. end
    """)
     
      while(decition != "4"):
        if (decition =="1")
            print(weightInitialpatients)
        elif (decition =="2")
        patientweight.append (input("add patient weight:"))
            
        listainicial.append (input("enter the new weight"))
        
        decition = int(input("""
    enter:
        1. to see patient weight and preasure
        2. to add patient new weight
        3. to see the higher preasure
        4. to see the lower preasure
        5. to know the total number of patients
        6. end
    """))
    return listainicial
pesos = complete_list (weightInitialpatients)
print (pesos)



