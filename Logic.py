#imports the necessary modules
import csvfilereader as cfr
import csv

#Logic for booking appointments
class appointment():
    
    #Initializing Fields
    def __init__(self,name,age,doctor,timeslot):
        self.name = name
        self.age = int(age)
        self.doctor = doctor
        self.timeslot = timeslot
        
    #Checks for any errors in fields
    def datachecker(self):
        class NumberError(Exception):
            pass
        class EmptyFieldError(Exception):
            pass

        try:
            # Check for empty fields
            if len(self.name) == 0 or len(self.doctor) == 0 or len(self.timeslot)==0 or not((0<self.age) and (self.age<=150)):
                raise EmptyFieldError

            # Check if name contains any digits
            if any(char.isdigit() for char in self.name):
                raise NumberError
            return True 
            
        except NumberError:
            return False
        
        except EmptyFieldError:
            return False

#Logic handling for doctor
class doctorLogic:

    #Loads the appointments for the doctor and returns a list
    def loadAppointments(drName):
        L = cfr.loadAppointments.load(drName)
        return L
    
    #Updates the appointment status to the required value
    def update_appointment_status(id,status):
        try:
            appointments = []
            with open("patientData.csv", "r") as data:
                appointments = list(csv.reader(data))
            with open("patientData.csv",'w',newline='') as data:
                writer = csv.writer(data)
                for row in appointments:
                    if row[1] == id:
                        row[4] = status
                writer.writerows(appointments)
        except:
            return False
    
    #Updates the appointment status to completed
    def complete_appointment(selected):
        try:
            appointment_id = selected[1]
            doctorLogic.update_appointment_status(appointment_id, "Completed")
            return True
        except:
            return False

    #Updates the appointment status to cancelled
    def cancel_appointment(selected):
        try:
            appointment_id = selected[1]
            doctorLogic.update_appointment_status(appointment_id,'Cancelled')
            return True
        except:
            return False
        
#Handles admin logic
class adminLogic:

    #Registers a doctor to the doctorCredentials.csv file
    def addDr(name,pswd):
        L = cfr.login.getDrNames()
        for i in L:
            if i[0] == name:
                return 0
        with open("doctorCredentials.csv","a",newline="") as data:
            data_writer = csv.writer(data)
            data_writer.writerow([name,pswd])
        return 1
    
    #Removes a doctor from the doctorCredentials.csv file
    def remDr(name,pswd):
        L = cfr.login.getDrNames()
        flag = 0
        with open("doctorCredentials.csv",'w',newline='') as f:
            w = csv.writer(f)
            for i in L:
                if i[0] == name and i[1] == pswd:
                    flag = 1
                else:
                    w.writerow(i)
        return flag
    
    #Opens the doctor gui
    def viewDr(name):
        L = cfr.login.getDrNames()
        for i in L:
            if i[0] == name:
                return 1
        return 0