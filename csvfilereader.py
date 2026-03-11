#importing the necessary modules
import csv
import os

#Custom Exception
class RepeatedDataError(Exception):
    pass

#All CSV file handling from patient
class AppointmentHistoryManager():

    #initializing patient data
    def __init__(self,name,age,doctor,timeslot):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.timeslot = timeslot
        self.status = "Booked"
        
    #Enters the data into the csv file
    def dataentry(self):
        with open("patientData.csv","a",newline="") as data:
            data_writer = csv.writer(data)
            data_writer.writerow([self.doctor,self.name,self.age,self.timeslot,self.status])
        return True
    
    #Checks for the correctness of entries, entered by the user
    def checker(self):
        result = os.path.exists("patientData.csv") #giving the name of the file as a parameter.
        if result == False:
            with open("patientData.csv", 'w',newline="") as fp:
                data_writer = csv.writer(fp)
                data_writer.writerow(["Doctor","Name","Age","Time Slot","Status"])
            return self.dataentry()
        else:
            with open("patientData.csv","r") as data:
                csv_reader = csv.DictReader(data)
                data = [row for row in csv_reader]
            try:
                for j in data:
                    if self.doctor == j["Doctor"] and self.timeslot == j["Time Slot"]:
                        raise RepeatedDataError
                return self.dataentry()
            except RepeatedDataError:
                return False

    #Updates the chat_data.csv file with patient and message
    def chat(doctor,message,patient):
        with open("chat_data.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Doctor", "Message", "Patient"])
            if os.stat("chat_data.csv").st_size == 0:  # Check if file is empty
                writer.writeheader()
            writer.writerow({"Doctor": doctor, "Message": message, "Patient": patient})

#Loads the appointments for doctor
class loadAppointments:

    def load(drName):
        L = []
        with open("patientData.csv", 'r') as f:
            r = list(csv.reader(f))[1:]
            for i in r:
                if i[0] == drName:
                    L.append(i)
        return L
    
#Used for login
class login:

    #checks if user and pswd match
    def login(user,pswd):
        with open('doctorCredentials.csv','r') as f:
            r = list(csv.reader(f))
        for i in r:
            if (i[0] == user) and (i[1] == pswd):
                return True
        return False
    
    #Returns a list with all the doctor names
    def getDrNames(): 
        with open('doctorCredentials.csv','r') as f:
            r = list(csv.reader(f))
        return r        
    
#return a final List(fL) which is a list of lists first element = name, second = message
class chat:
    def getMSG(drName):
        fL = []

        with open('chat_data.csv','r') as f:
            x = list(csv.reader(f))[1:]
            L =[]
            for i in x:
                if i[0] == drName:
                    L.append([i[2],i[1]])

        with open('patientData.csv','r') as f:
            y = list(csv.reader(f))[1:]
            for i in y:
                if (i[1] in [j[0] for j in L]) and (drName == i[0]) and (i[-1] == 'Booked'):
                    for j in L:
                        if j[0] == i[1]:
                            fL.append([i[1],j[1]])

        return fL