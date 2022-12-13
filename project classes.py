class Doctor:
    
    def __init__(self):
        self.id = "None"
        self.name = "None"
        self.spec = "None"
        self.hours = "None"
        self.qual = "None"
        self.room = "None"

    def formatDrInfo(self,list_to_convert):
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'

    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n\n")
        self.name = input("Enter the doctor's name:\n\n")
        self.spec = input("Enter the doctor's specility:\n\n")
        self.hours = input("Enter the doctor's timing (e.g., 7am-10pm):\n\n")
        self.qual = input("Enter the doctor's qualification:\n\n")
        self.room = input("Enter the doctor's room number:\n\n")
        return [self.id,self.name,self.spec,self.hours,self.qual,self.room]

    def readDoctorsFile(self):
        self.open_file = open("files\doctors.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def searchDoctorById(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        
        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor ID:\n\n")
        
        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.displayDoctorInfo(self.new_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system")

    def searchDoctorByName(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor name:\n\n")
        
        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][1] == self.query:
                self.displayDoctorInfo(self.new_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same name on the system")
        
    def displayDoctorInfo(self,doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper() 
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        print(f"{self.doctor_list[0]: <5}{self.doctor_list[1]: <20}{self.doctor_list[2]: <15}{self.doctor_list[3]: <15}{self.doctor_list[4]: <15}{self.doctor_list[5]: <0}")

    def editDoctorInfo(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")

        self.query = input("Please enter the id of the doctor that you want to edit their information:\n\n")
        
        self.flag = False
        for i in range(len(self.new_list)):
            if self.new_list[i][0] == self.query:
                self.new_list[i][1] = input("\nEnter new Name:\n\n")
                self.new_list[i][2] = input("\nEnter new Specilist in:\n\n")
                self.new_list[i][3] = input("\nEnter new Timing: \n\n")
                self.new_list[i][4] = input("\nEnter new Qualification: \n\n")
                self.new_list[i][5] = input("\nEnter new Room number:\n\n")
                self.doctor_list[i] = self.formatDrInfo(self.new_list[i])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []

        for i in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[i] = self.doctor_list[i].split("_")
        
        del self.new_list[0] 
    
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        for i in range(len(self.new_list)):
            print(f"{self.new_list[i][0]: <5}{self.new_list[i][1]: <20}{self.new_list[i][2]: <15}{(self.new_list[i][3].lower()): <15}{(self.new_list[i][4].upper()): <15}{self.new_list[i][5]: <0}")

    def writeListOfDoctorsToFile(self,doctor_list):
        self.open_file = open("files\doctors.txt", "w")
        self.index = 0
        for entries in doctor_list:
            self.open_file.write(doctor_list[self.index])
            self.index +=1
        self.open_file.close()

    def addDrToFile(self):
        self.doctor_to_add = self.enterDrInfo()
        self.doctor_to_add = self.formatDrInfo(self.doctor_to_add)
        self.doctor_list = self.readDoctorsFile()
        
        self.index = 0
        for entries in self.doctor_list:
            if self.doctor_list[self.index].endswith('\n') == False:
                self.doctor_list[self.index] = self.doctor_list[self.index] + '\n'
            self.index += 1

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list)

class Facility:
    
    def __init__(self):
        self.facility_name = "None"

    def addFacility(self):
        '''Adds and writes the facility name to the file'''
        self.open_file = open("files\facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()
        
        self.facility_name = input("Enter Facility name: \n\n")
        
        self.facility_list.append(self.facility_name)

        self.writeListOffacilitiesToFile(self.facility_list)

    def displayFacilities(self):
        '''Displays the list of facilities'''
        self.open_file = open("files\facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()

        self.facility_list[0] = "The " + self.facility_list[0]
        
        for i in range(len(self.facility_list)):
            if self.facility_list[i].endswith('\n') == False:
                print(self.facility_list[i]+'\n')
            else:
                print(self.facility_list[i])

    def writeListOffacilitiesToFile(self,new_entry):
        '''Writes the facilities list to facilities.txt'''
        self.open_file = open("files\facilities.txt", "w")
  
        self.index = 0
        for entries in new_entry:
            if new_entry[self.index].endswith('\n') == False:
                new_entry[self.index] = new_entry[self.index] + '\n'
            self.open_file.write(new_entry[self.index])
            self.index += 1

        self.open_file.close()

class Laboratory:

    def __init__(self, Name, Cost):
        self.Name = Name
        self.Cost = Cost
    
    def formatLabInfo(self):
        return f"{self.Name}_{self.Cost}"

    def enterLaboratoryInfo(self):
        self.Name = input("Enter Laboratory Name: ")
        self.Cost = input("Enter Laboratory Cost: ")

    def readLaboratoriesFile(self, file_name):
        labs_list = []
        with open(file_name, "r") as file:
            for line in file:
                lab_info = line.split("_")
                labs_list.append(self.__init__(lab_info[0], lab_info[1]))
        return labs_list

    def addLabToFile(self, file_name):
        with open(file_name, "a") as file:
            self.enterLaboratoryInfo()
            file.write(self.formatLabInfo() + "\n")

    def writeListOfLabsToFile(self, labs_list, file_name):
        with open(file_name, "w") as file:
            for lab in labs_list:
                file.write(lab.formatLabInfo() + "\n")
    
    def displayLabsList(self, labs_list):
        print("Laboratories: ")
        for lab in labs_list:
            print(lab.Name)


class Patient:

    def __init__(self, pid, Name, Disease, Gender, Age):
        self.pid = pid
        self.Name = Name
        self.Disease = Disease
        self.Gender = Gender
        self.Age = Age
    
    def formatPatientInfo(self):
        return f"{self.pid}_{self.Name}_{self.Disease}_{self.Gender}_{self.Age}"

    def enterPatientInfo(self):
        self.pid = input("Enter Patient ID: ")
        self.Name = input("Enter Patient Name: ")
        self.Disease = input("Enter Patient Disease: ")
        self.Gender = input("Enter Patient Gender: ")
        self.Age = input("Enter Patient Age: ")

    def readPatientsFile(self, file_name):
        patients_list = []
        with open(file_name, "r") as file:
            for line in file:
                patient_info = line.split("_")
                patients_list.append(self.__init__(patient_info[0], patient_info[1], patient_info[2], patient_info[3], patient_info[4]))
        return patients_list

    def searchPatientById(self, id, patients_list):
        for patient in patients_list:
            if patient.pid == id:
                return patient
        return None

    def displayPatientInfo(self):
        print(f"Patient ID: {self.pid}")
        print(f"Patient Name: {self.Name}")
        print(f"Patient Disease: {self.Disease}")
        print(f"Patient Gender: {self.Gender}")
        print(f"Patient Age: {self.Age}")

    def editPatientInfo(self, id, patients_list):
        index = -1
        for i in range(len(patients_list)):
            if patients_list[i].pid == id:
                index = i
        if index == -1:
            return False
        self.enterPatientInfo()
        patients_list[index] = self
        return True

    def displayPatientsList(self, patients_list):
        for patient in patients_list:
            patient.displayPatientInfo()
            print()

    def writeListOfPatientsToFile(self, patients_list, file_name):
        with open(file_name, "w") as file:
            for patient in patients_list:
                file.write(patient.formatPatientInfo() + "\n")
    
    def addPatientToFile(self, file_name):
        with open(file_name, "a") as file:
            self.enterPatientInfo()
            file.write(self.formatPatientInfo() + "\n")


class Management:
    
    def Display_Menu(self):
        self.repeat = True
        while self.repeat:
            self.option = input('Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n')
            
            if int(self.option) == 1:
                self.cycle = True
                self.obj_handle = Doctor()
                while self.cycle:
                    self.option = input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 6:
                        self.cycle = False
                        print("")

            elif int(self.option) == 2:
                self.cycle = True
                self.obj_handle = Facility()
                while self.cycle:
                    self.option = input('Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the previous Menu") 
                    elif int(self.option) == 2:
                        self.obj_handle.addFacility()
                        print("\nBack to the previous Menu") 
                    elif int(self.option) == 3:
                        self.cycle = False
                        print("")
            
            else:
                self.repeat = False   

            if int(self.option) == 3:
                self.cycle = True
                self.obj_handle = Laboratory()
                while self.cycle:
                    self.option = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.displayLabsList()
                    elif int(self.option) == 2:
                        self.obj_handle.addLabToFile()
                    elif int(self.option) == 3:
                        self.cycle = False
                    print("Back to the previous Menu\n") 
            
            elif int(self.option) == 4:
                self.cycle = True
                self.obj_handle = Patient()
                while self.cycle:
                    self.option = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n')
                    if int(self.option) == 1:
                        self.obj_handle.ddisplayPatientsList()
                    elif int(self.option) == 2:
                        self.obj_handle.searchPatientById()
                    elif int(self.option) == 3:
                        self.obj_handle.addPatientToFile()
                    elif int(self.option) == 4:
                        self.obj_handle.editPatientInfo()
                    elif int(self.option) == 5:
                        self.cycle = False
                    print("Back to the previous Menu\n")  
       

run_obj = Management()
run_obj.Display_Menu()
