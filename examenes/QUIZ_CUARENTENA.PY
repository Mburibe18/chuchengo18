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
     
        weight_1 =32
     preasure_1= (6*weight_1)
        weight_2 =64
     preasure_2= (6*weight_2)
        weight_3= 74
     preasure_3= (6*weight_3)
        weight_4= 85
     preasure_4= (6*weight_4)
        weight_5 =98
     preasure_5= (6*weight_5)
        weight_6= 115
     preasure_6= (6*weight_6)
        weight_7= 122
     preasure_7= (6*weight_7)
        weight_8 =127
     preasure_8= (6*weight_8)
        weight_9= 137
     preasure_9= (6*weight_9)
        weight_10= 148
     preasure_10= (6*weight_10)

     print (preasure_1,preasure_2,preasure_3,preasure_4,preasure_5,preasure_6,preasure_7,preasure_8,preasure_9,preasure_10)

     


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



