import Read_Studio_Excel_Sheet
import Write_Studio_Excel_Sheet


def AppointmentIndexInCoachesDataBase (member_ID) :
  for i in Coaches_DataBase :
        for j in Coaches_DataBase[i] :							
                if str(member_ID) == str(j[0]) :
                        Appointment_index = Coaches_DataBase[i].index(j)
                        return Appointment_index,i

print("****************************************************************************")
print("                                                                           ")
print("                          Welcome to KG Hospital.                          ")
print("                                                                           ")
print("           Please edit the code as per needs as this is just a model       ")
print("                                                                           ")
print("                     Note: Members=Patients, Coaches=Doctors               ")
print("                                                                           ")
print("                                                                           ")
print("                                                         -Kapil, Gandharva ")
print("****************************************************************************")


tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

        Members_DataBase = Read_Studio_Excel_Sheet.Read_Members_DataBase()
        Coaches_DataBase  = Read_Studio_Excel_Sheet.Read_Coaches_DataBase()
                        
        print("-----------------------------------------")
        print("|Enter 1 for Admin mode			|\n|Enter 2 for patient mode			|")
        print("-----------------------------------------")
        Admin_user_mode = input("Enter your mode : ") 
        

        if Admin_user_mode == "1" :																			#Admin mode
                        print("*****************************************\n|         Welcome to Admin mode         |\n*****************************************")
                        Password = input("Please enter your password : ")
                        while True :
                                
                                if Password == "123445" :
                                        print("-----------------------------------------")
                                        print("|To manage patients Enter 1 		|\n|To manage doctors Enter 2	 	|\n|To manage appointments Enter 3 	|\n|To be back Enter E			|")
                                        print("-----------------------------------------")
                                        AdminOptions = input ("Enter your choice : ")
                                        AdminOptions = AdminOptions.upper()
                                        
                                        if AdminOptions == "1" :															#Admin mode --> Members Management
                                                        print("-----------------------------------------")
                                                        print("|To add new patient Enter 1	  	|")
                                                        print("|To display patient Enter 2	  	|")
                                                        print("|To delete patient data Enter 3		|")
                                                        print("|To edit patient data Enter 4    	|")
                                                        print("|To Back enter E      			|")
                                                        print("-----------------------------------------")
                                                        Admin_choice = input ("Enter your choice : ")
                                                        Admin_choice = Admin_choice.upper()
                                                        
                                                        if Admin_choice == "1" : 										#Admin mode --> Members Management --> Enter new patient data
                                                                                try :		#To avoid non integer input
                                                                                        member_ID = int(input("Enter patient ID : "))
                                                                                        while member_ID in Members_DataBase :		#if Admin entered used ID
                                                                                                member_ID = int(input("This ID is unavailable, please try another ID : "))					
                                                                                        Programme=input("Enter patient department                : ")
                                                                                        CoachName=input("Enter name of doctor guiding the patient : ")
                                                                                        Name      =input("Enter patient name                      : ")
                                                                                        Age       =input("Enter patient age                       : ")
                                                                                        Gender    =input("Enter patient gender                   : ")
                                                                                        Address   =input("Enter patient address                   : ")
                                                                                        OriginalWeight =input("Enter patient original weight                  : ")
                                                                                        CurrentWeight =input("Enter patient current weight                   : ")
                                                                                        PhoneNumber=input("Enter patient phone number               : ")
                                                                                        Members_DataBase[member_ID]=[Programme,CoachName,Name,Age,Gender,Address,OriginalWeight,CurrentWeight,PhoneNumber]
                                                                                        print("----------------------Patient added successfully----------------------")
                                                                                except :
                                                                                        print("Patient ID should be an integer number")
                                                                        
                                                        elif Admin_choice == "2" :										#Admin mode -->  Members Management --> Display patient data
                                                                                try :		#To avoid non integer input
                                                                                        member_ID = int(input("Enter patient ID : "))
                                                                                        while member_ID not in Members_DataBase :
                                                                                                member_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                                                        print("\nPatient name        : ",Members_DataBase[member_ID][2])
                                                                                        print("Patient age         : ",Members_DataBase[member_ID][3])
                                                                                        print("Patient gender      : ",Members_DataBase[member_ID][4])
                                                                                        print("Patient address     : ",Members_DataBase[member_ID][5])
                                                                                        print("Patient original weight     : ",Members_DataBase[member_ID][6])
                                                                                        print("Patient current weight     : ",Members_DataBase[member_ID][7])
                                                                                        print("Patient phone number : ",Members_DataBase[member_ID][8])
                                                                                        print("Patient is in "+Members_DataBase[member_ID][0]+" department")
                                                                                        print("Patient is followed by doctor : "+Members_DataBase[member_ID][1])
                                                                                except :
                                                                                        print("Patient ID should be an integer number")
                                                        
                                                        elif Admin_choice == "3" :										#Admin mode --> Members Management --> Delete patient data
                                                                                try :		#To avoid non integer input
                                                                                        member_ID = int(input("Enter patient ID : "))
                                                                                        while member_ID not in Members_DataBase :
                                                                                                member_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                                                        Members_DataBase.pop(member_ID)
                                                                                        print("----------------------Patient data deleted successfully----------------------")
                                                                                except :
                                                                                        print("Patient ID should be an integer number")
                                                        elif Admin_choice =="4":
                                                                                try:            #To avoid non integer input
                                                                                        member_ID = int(input("Enter patient ID: "))
                                                                                        while member_ID not in Members_DataBase:
                                                                                                member_ID = int(input("Incorrect ID, Please Enter patient ID: "))
                                                                                        while True:
                                                                                                print("------------------------------------------")
                                                                                                print("|To edit patient department Enter 1 :      |")
                                                                                                print("|To edit doctor for the department Enter 2 :   |")
                                                                                                print("|To edit patient Name Enter 3 :           |")
                                                                                                print("|To edit patient Age Enter 4 :            |")
                                                                                                print("|To edit patient Gender Enter 5 :         |")
                                                                                                print("|To edit patient Address Enter 6 :        |")
                                                                                                print("|To edit patient Current Weight Enter 8:  |")
                                                                                                print("|To edit patient Phone Number Enter 9 :   |")
                                                                                                print("|To be Back Enter E                      |")
                                                                                                print("------------------------------------------")
                                                                                                Admin_choice = input("Enter your choice : ")
                                                                                                Admin_choice = Admin_choice.upper()
                                                                                                if Admin_choice == "1" :
                                                                                                        Members_DataBase[member_ID][0]=input("\nEnter patient department : ")
                                                                                                        print("----------------------Patient department edited successfully----------------------")
                                                                                                        
                                                                                                elif Admin_choice == "2" :
                                                                                                        Members_DataBase[member_ID][1]=input("\nEnter doctor following case : ")
                                                                                                        print("----------------------Doctor for department edited successfully----------------------")
                                                                        
                                                                                                elif Admin_choice == "3" :
                                                                                                        Members_DataBase[member_ID][2]=input("\nEnter patient name : ")
                                                                                                        print("----------------------Patient name edited successfully----------------------")
                                                                                                
                                                                                                elif Admin_choice == "4" :
                                                                                                        Members_DataBase[member_ID][3]=input("\nEnter patient Age : ")
                                                                                                        print("----------------------Patient age edited successfully----------------------")
                                                                                        
                                                                                                elif Admin_choice == "5" :
                                                                                                        Members_DataBase[member_ID][4]=input("\nEnter patient gender : ")
                                                                                                        print("----------------------Patient gender successfully----------------------")
                                                                                                        
                                                                                                elif Admin_choice == "6" :
                                                                                                        Members_DataBase[member_ID][5]=input("\nEnter patient address : ")
                                                                                                        print("----------------------Patient address edited successfully----------------------")
                                                                                                elif Admin_choice == "7" :
                                                                                                        Members_DataBase[member_ID][6]=input("\nEnter patient original weight : ")
                                                                                                        print("----------------------Patient original weight edited successfully----------------------")
                                                                                                elif Admin_choice == "8" :
                                                                                                        Members_DataBase[member_ID][7]=input("\nEnter patient current weight : ")
                                                                                                        print("----------------------Patient current weight edited successfully----------------------")
                                                                                                        
                                                                                                elif Admin_choice == "9" :
                                                                                                        Members_DataBase[member_ID][8]=input("\nEnter patient Phone Number : ")
                                                                                                        print("----------------------Patient Phone Number edited successfully----------------------")
                                                                                        
                                                                                                elif Admin_choice == "E" :
                                                                                                        break
                                                                                                        
                                                                                                else :
                                                                                                        print("Please Enter a correct choice")
                                                                                except :
                                                                                        print("Patient ID should be an integer number")
                                                                                                                                                        
                                                        elif Admin_choice == "E" :										#Admin mode --> Members Management --> Back
                                                                                break
                                                        
                                                        else :
                                                                                print("Please enter a correct choice\n")
                                                                                
                                        elif AdminOptions == "2" :															#Admin mode --> Coaches Management
                                                print("-----------------------------------------")
                                                print("|To add new doctor  Enter 1              |")
                                                print("|To display doctor  Enter 2              |")
                                                print("|To delete doctor  data Enter 3          |")
                                                print("|To edit doctor  data Enter 4            |")
                                                print("|To be back enter E                     |")
                                                print("-----------------------------------------")
                                                Admin_choice = input ("Enter your choice : ")
                                                Admin_choice = Admin_choice.upper()
                                                
                                                if Admin_choice == "1" : 											#Admin mode --> doctores Management --> Enter new doctor data
                                                                try :		#To avoid non integer input
                                                                        Coach_ID = int(input("Enter doctor ID : "))
                                                                        while Coach_ID in Coaches_DataBase :			#if Admin entered used ID
                                                                                Coach_ID = int(input("This ID is unavailable, please try another ID : "))
                                                                        
                                                                        Name      =input("Enter doctor name       : ")
                                                                        Address   =input("Enter doctor address    : ")
                                                                        PhoneNumber =input("Enter doctor phone number    : ")
                                                                        Coaches_DataBase[Coach_ID]=[[Name,Address,PhoneNumber]]
                                                                        print("----------------------Doctor added successfully----------------------")
                                                                except :
                                                                        print("Doctor ID should be an integer number")
                                                        
                                                elif Admin_choice == "2" : 											#Admin mode --> Coaches Management --> Display doctor data
                                                                try :		#To avoid non integer input
                                                                        Coach_ID = int(input("Enter doctor ID : "))
                                                                        while Coach_ID not in Coaches_DataBase :
                                                                                Coach_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                                                        print("Doctor name    : ",Coaches_DataBase[Coach_ID][0][0])
                                                                        print("Doctor address : ",Coaches_DataBase[Coach_ID][0][1])
                                                                        print("Doctor phone number : ",Coaches_DataBase[Coach_ID][0][2])
                                                                except :
                                                                        print("Doctor ID should be an integer number")
                                                
                                                elif Admin_choice == "3" :											#Admin mode --> Coaches Management --> Delete doctor data
                                                                try :		#To avoid non integer input
                                                                        Coach_ID = int(input("Enter doctor ID : "))
                                                                        while Coach_ID not in Coaches_DataBase :
                                                                                Coach_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                                                        Coaches_DataBase.pop(Coach_ID)
                                                                        print("/----------------------Doctor data deleted successfully----------------------/")
                                                                except :
                                                                        print("Doctor ID should be an integer number")

                                                elif Admin_choice == "4" :											#Admin mode --> Coaches Management --> Edit doctor data
                                                                try :		#To avoid non integer input	
                                                                        Coach_ID=input("Enter doctor ID : ")
                                                                        while Coach_ID not in Coaches_DataBase :
                                                                                Coach_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                                                        print("-----------------------------------------")
                                                                        print("|To Edit doctor's name Enter 1    |")
                                                                        print("|To Edit doctor's address Enter 2          |")
                                                                        print("|To Edit doctor's phone number Enter 3       |")
                                                                        print("To be Back Enter E                      |")
                                                                        print("-----------------------------------------")
                                                                        Admin_choice=input("Enter your choice : ")
                                                                        Admin_choice = Admin_choice.upper()
                                                                        if Admin_choice == "1" :
                                                                                Coaches_DataBase[Coach_ID][0][0]=input("Enter Doctor's Name : ")
                                                                                print("/----------------------Doctor's name edited successfully----------------------/")
                                                                                
                                                                        elif Admin_choice == "2" :
                                                                                Coaches_DataBase[Coach_ID][0][1]=input("Enter doctor's Address : ")
                                                                                print("----------------------Doctor's address edited successfully----------------------")
                                                                                
                                                                        elif Admin_choice == "3" :
                                                                                Coaches_DataBase[Coach_ID][0][2]=input("Enter doctor's Phone Number : ")
                                                                                print("----------------------Doctor's phone number edited successfully----------------------")
                                                                        
                                                                        elif Admin_choice == "E" :
                                                                                break
                                                                        
                                                                        else :
                                                                                print("\nPlease enter a correct choice\n")
                                                                                
                                                                except :
                                                                        print("doctor ID should be an integer number")
                                                                                
                                                elif Admin_choice == "E" :											#Back
                                                                        break
                                                                
                                                else :
                                                        print("\nPlease enter a correct choice\n")
                                                                                
                                        elif AdminOptions == "3" :															#Admin mode --> Appointment Management
                                                print("-----------------------------------------")
                                                print("|To book an appointment Enter 1         |")
                                                print("|To edit an appointment Enter 2         |")
                                                print("|To cancel an appointment Enter 3       |")
                                                print("|To be back enter E                     |")
                                                print("-----------------------------------------")
                                                Admin_choice = input ("Enter your choice : ")
                                                Admin_choice = Admin_choice.upper()
                                                if Admin_choice == "1" :												#Admin mode --> Appointment Management --> Book an appointment							
                                                        try :		#To avoid non integer input
                                                                        Coach_ID = int(input("Enter the ID of doctor : "))
                                                                        while Coach_ID not in Coaches_DataBase :
                                                                                Coach_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
                                                                        print("---------------------------------------------------------")
                                                                        print("|For book an appointment for an existing patient Enter 1   |\n|For booking an appointment for a new patient Enter 2      |\n|To be Back Enter E                                     |")
                                                                        print("---------------------------------------------------------")
                                                                        Admin_choice = input ("Enter your choice : ")
                                                                        Admin_choice = Admin_choice.upper()
                                                                        if Admin_choice == "1" :
                                                                                        member_ID = int(input("Enter patient ID : "))
                                                                                        while member_ID not in Members_DataBase :		#if Admin entered incorrect ID
                                                                                                member_ID = int(input("Incorrect ID, please Enter a correct patient ID : "))	
                                                                        
                                                                                
                                                                        elif Admin_choice == "2" :
                                                                                member_ID = int(input("Enter patient ID : "))
                                                                                while member_ID in Members_DataBase :		#if Admin entered used ID
                                                                                        member_ID = int(input("This ID is unavailable, please try another ID : "))					
                                                                                DoctorName=Coaches_DataBase[Coach_ID][0][0]
                                                                                Name      =input("Enter patient name    : ")
                                                                                Age       =input("Enter patient age     : ")
                                                                                Gender    =input("Enter patient gender  : ")
                                                                                Address   =input("Enter patient address : ")
                                                                                OriginalWeight= input("Enter patient original weight : ")
                                                                                PhoneNumber=input("Enter patient phone number")
                                                                                Members_DataBase[member_ID]=[DoctorName,Name,Age,Gender,Address,OriginalWeight,PhoneNumber]
                                                                        
                                                                        elif Admin_choice == "E" :
                                                                                break
                                                                                
                                                                        Session_Start = input("Session starts at : ")
                                                                        while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
                                                                                Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
                                                                                
                                                                        for i in Coaches_DataBase[Coach_ID] :
                                                                                if type(i[0])!=str :
                                                                                        while Session_Start >= i[1] and Session_Start < i[2] :
                                                                                                Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
                                                                        Session_End   = input("Session ends at : ")
                                                                        
                                                                        New_Appointment=list()
                                                                        New_Appointment.append(member_ID)
                                                                        New_Appointment.append(Session_Start)
                                                                        New_Appointment.append(Session_End)
                                                                        Coaches_DataBase[Coach_ID].append(New_Appointment)								
                                                                        print("/----------------------Appointment booked successfully----------------------/")
                                                        except :
                                                                        print("Doctor ID should be an integer number")
                                
                                                elif Admin_choice == "2" :												#Admin mode --> Appointment Management --> Edit an appointment
                                                                try :		#To avoid non integer input
                                                                        member_ID = int(input("Enter patient ID : "))						
                                                                        while member_ID not in Members_DataBase :
                                                                                member_ID = int(input("Incorrect Id, Please Enter correct patient ID : "))
                                                                        try :   #To avoid no return function
                                                                                        AppointmentIndex,PairKey = AppointmentIndexInCoachesDataBase(Coach_ID)
                                                                                        Session_Start = input ("Please enter the new start time : ")
                                                                                        while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
                                                                                                Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
                                                                                                
                                                                                        for i in Coaches_DataBase[Coach_ID] :
                                                                                                if type(i[0])!=str :
                                                                                                        while Session_Start >= i[1] and Session_Start < i[2] :
                                                                                                                Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
                                                                                        Session_End = input ("Please enter the new end time : ")
                                                                                        Coaches_DataBase[PairKey][AppointmentIndex]=[member_ID,Session_Start,Session_End]							
                                                                                        print("/----------------------appointment edited successfully----------------------/")
                                                                        except :
                                                                                        print("No Appointment for this patient")
                                                                except :
                                                                        print("doctor ID should be an integer number")
                                        
                                                elif Admin_choice == "3" :												#Admin mode --> Appointment Management --> Cancel an appointment
                                                                try :		#To avoid non integer input
                                                                        member_ID = int(input("Enter patient ID : "))
                                                                        while member_ID not in Members_DataBase :
                                                                                member_ID = int(input("Incorrect ID, Enter patient ID : "))
                                                                        try :
                                                                                        AppointmentIndex,PairKey = AppointmentIndexInCoachesDataBase(member_ID)						
                                                                                        Coaches_DataBase[PairKey].pop(AppointmentIndex)
                                                                                        print("/----------------------appointment canceled successfully----------------------/")
                                                                        except :
                                                                                        print("No Appointment for this patient")
                                                                except :	 #To avoid no return function
                                                                        print("Patient ID should be an integer number")
                                                
                                                elif Admin_choice == "E" :												#Back
                                                                        break
                                                
                                                else :
                                                                        print("please enter a correct choice")
                                        
                                        elif AdminOptions == "E" :															#Back
                                                break
                                        
                                        else :
                                                print("Please enter a correct option")
                                
                        
                                elif Password != "123445" :
                                        if tries < 2 :
                                                Password = input("Password incorrect, please try again : ")
                                                tries += 1
                                        else :
                                                print("Incorrect password, no more tries")
                                                tries_flag = "Close the program"
                                                break
                        
                                Write_Studio_Excel_Sheet.Write_Members_DataBase(Members_DataBase)
                                Write_Studio_Excel_Sheet.Write_Coaches_DataBase(Coaches_DataBase)
                                
                                
        elif Admin_user_mode == "2" :																		#User mode
                print("****************************************\n|         Welcome to user mode         |\n****************************************")
                while True :
                        print("\n-----------------------------------------")
                        print("|To view Hospital's doctors names Enter 1 |")
                        print("|To view Hospital's doctors info Enter 2     |")
                        print("|To view hospital's patients Enter 3    |")
                        print("|To view patients's details Enter 4      |")
                        print("|To view doctors's appointments Enter 5  |")
                        print("|To be Back Enter E                     |")
                        print("-----------------------------------------")
                        UserOptions = input("Enter your choice : ")
                        UserOptions = UserOptions.upper()
                        
                        if   UserOptions == "1" :											#User mode --> view studio's departments
                                                print("Hospital doctors :")
                                                for i in Coaches_DataBase :
                                                        print("	"+Coaches_DataBase[i][0][0])
                                
                        elif UserOptions == "2" :											#User mode --> view studio's Coaches
                                                print("Hospital's doctors :")
                                                for i in Coaches_DataBase :
                                                        print("	Name : "+Coaches_DataBase[i][0][0], "Address : "+Coaches_DataBase[i][0][1],"Phone Number :"+Coaches_DataBase[i][0][2])
                                                        
                        elif UserOptions == "3" :											#User mode --> view members residents
                                for i in Members_DataBase :
                                        print("	Patient : "+Members_DataBase[i][2]+" in "+Members_DataBase[i][0]+" department and followed by "+Members_DataBase[i][1]+", age : "+Members_DataBase[i][3]+", from : "+Members_DataBase[i][5]+", Phone Number :"+Members_DataBase[i][8])
                        
                        elif UserOptions == "4" :											#User mode --> view members details
                                try :				#To avoid non integer input
                                        member_ID = int(input("Enter patient's ID : "))
                                        while member_ID not in Members_DataBase :
                                                member_ID = int(input("Incorrect Id, Please enter patient ID : "))
                                        print("	patient name        : ",Members_DataBase[member_ID][2])
                                        print("	patient age         : ",Members_DataBase[member_ID][3])
                                        print("	patient gender      : ",Members_DataBase[member_ID][4])
                                        print("	patient address     : ",Members_DataBase[member_ID][5])
                                        print("	patient original weight     : ",Members_DataBase[member_ID][6])
                                        print("	patient current weight     : ",Members_DataBase[member_ID][7])
                                        print("	patient phone number : ",Members_DataBase[member_ID][8])
                                        print("	patient is in "+Members_DataBase[member_ID][0]+" department")
                                        print("	patient is followed by doctor : "+Members_DataBase[member_ID][1])
                                except :
                                        print("Patient ID should be an integer number")
                                                
                        elif UserOptions == "5" :											#User mode --> view doctor's appointments
                                try :				#To avoid non integer input
                                        Coach_ID = int(input("Enter doctor's ID : "))
                                        while Coach_ID not in Coaches_DataBase :
                                                Coach_ID = int(input("Incorrect Id, Please enter doctor ID : "))
                                        print(Coaches_DataBase[Coach_ID][0][0]+" has appointments :")
                                        for i in Coaches_DataBase[Coach_ID] :
                                                if type(i[0])==str :
                                                        continue
                                                else :
                                                        print("	from : "+i[1]+"    to : "+i[2])
                                except :
                                        print("doctor ID should be an integer number")
                                
                        elif UserOptions == "E" :											#Back
                                break
                                
                        else :
                                print("Please Enter a correct choice")
                                
                                
        else :
                print("Please choice just 1 or 2")
