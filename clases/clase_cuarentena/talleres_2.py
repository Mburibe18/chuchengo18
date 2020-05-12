MENSAJE_OF_ENTRANCE ="Hi , welcome to this hospital"

print (MENSAJE_OF_ENTRANCE)


_decition = int (input("""
    enter the number :
    1- to know the list of our doctors , nurses and patients
    2- to see patients status
    3- to create a new list of persons
    4- log out
"""))
while (_decition != 4):
    if (_decition == 1):
        def show_three_lists ( list_number_1 , list_number_2 , list_number_3):
            if ( len ( list_number_1 ) ==  len ( list_number_2) == len (list_number_3)):
                print ("doctors -" , "nurses -" , "patients")
                for i  in range ( len ( list_number_1 )):
                    print ( list_number_1 [ i ] , list_number_2 [ i ] , list_number_3 [i])

            
    

        doctors = ["Mafe --", "Elena --", "Ysabella --", "The teacher --", "Marco --"]
        nurses = ["Santiago --", "Valeria --", "Santiago H --", "Daniel Zarate --", "Camila Herrera M --"]
        patients = ["Camila Herrera B", "  Juanes", "Ines", "Benito", "Dubeimar"]   

        show_three_lists (doctors , nurses , patients)
        
    elif (_decition == 2):
        def show_two_lists ( list_number_1 , list_number_2):
            if ( len ( list_number_1 ) ==  len ( list_number_2 )):
                print ("paatients -" , "status")
                for i  in range ( len ( list_number_1 )):
                    print ( list_number_1 [ i ] , list_number_2 [ i ])

        patients = ["Jimena --", "Mateo --", "Ricardo --", "Antonia --", "Fredy --"] 
        status = ["UCI", "SERIOUS", "SERIOUS", "STABLE", "UCI"]

        show_two_lists (patients, status)


    elif (_decition == 3):
        def completelist ():
            list = []
            decition = input ("enter y--> to add more persons n--> for no to add more people : ")
            while (decition == "y"):
                list.append (input("enter a person in the list : "))
                decition = input ("enter y--> to add more people n--> for no to add more people : ")
            return list 
        print ("enter the doctors list : ")
        doctors = completelist ()
        print ("enter nurses list : ")
        nurses = completelist ()
        print ("enter the patients list : ")
        patients = completelist ()
        
        show_three_lists (doctors, nurses, patients)

    
    else:
        print("enter a valid value")

    _decision = int (input("""
      ingrese :
        1- to know the list of our doctors , nurses and patients
        2- to see patients status
        3- to create a new list of persons
        4- log out
        """))
print("thanks for using the program bro")