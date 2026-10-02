from abc import ABC, abstractmethod
# Abstraction
class Person(ABC):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass


# Inheritance

class Patient(Person):
    def __init__(self,patient_id, name, age, desease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.desease = desease
        self.__bill = 0
        # Encapsulation
    def add_bill(self,amount):
        self.__bill += amount

    def get_bill(self):
        return self.__bill
    def display_info(self):
        print(f"Patient Id :,{self.patient_id}")
        print(f"Name: {self.name}")
        print(f"age:{self.age}")
        print(f"Disease: {self.desease}")
        print(f"Bill : Rs{self.__bill}")
class Doctor(Person):
    def __init__(self, doctor_id, name, age,specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Neme : {self.name}")
        print(f"Age: {self.age}")
        print(f" Specialization : {self.specialization}")

# hospitral management System

class Hospitals:
    def __init__(self,name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patients addes succesfully..")


    def add_doctor(self, patient):
        self.doctors.append(Doctor)
        print("Doctors Added Successfully!")

    def show_patients(self):
        print("\n patients Details")
        for patient in self.patients:
            patient.display_info()
            print()

    def show_doctors(self):
            print("\n Doctors Details")
            for doctor in self.doctors:
                doctor.display_info()
                print()

    def discharge_patient(self,patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"Patient {patient_id} Discharged")
                return
            print("Patient not Found....")



# main program

Hospitals = Hospitals("City care Hospiltals")
# Creating Object
Doctor1 = Doctor(101,"DR. Rama",45,"Nuerologist")
Doctor2 = Doctor(102,"DR Rao",55, "Cardiologist")

Patient1 = Patient(1001,"Rahul",30,"Heart Problem")
Patient2  = Patient(1002,"Sona",32,"Migrain")
# adding doctors and patient
Hospitals.add_doctor(Doctor1)
Hospitals.add_doctor(Doctor2)

Hospitals.add_patient(Patient1)
Hospitals.add_patient(Patient2)
# adding bills
Patient1.add_bill(500000)
Patient1.add_bill(25000)


Patient2.add_bill(100000)

# display Information
#Hospitals.show_doctors()
Hospitals.show_patients()
#Hospitals.show_doctors()

# Discharge patient
Hospitals.discharge_patient(2)






