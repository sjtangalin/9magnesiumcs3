
# Parent Class
# This is yung main class for all patient types.
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # Getters and setters so that you can access and update ang data.
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # Regular patients pay the full amount.
    def calculate_bill(self):
        return self.__bill_amount

    # Displays the patient's type.
    def display_patient_type(self):
        print("Patient Type: Regular Patient")


# Senior Patient
# Inherits from Patient, with a 20% discount.
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    # Method overriding para senior citizen is yung ma-display.
    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


# PhilHealth Patient
# Inherits from Patient, with a 15% discount.
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    # Same method, but different patient type naman.
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


# Creating objects for each patient type.
# Each object represents a different patient.
patients = [
    Patient("Juan Dela Cruz", 15000),
    SeniorPatient("Pedro Santos", 15000),
    PhilHealthPatient("Maria Reyes", 15000)
]


# for loop so that automatic ma-display lahat ng patients.
for patient in patients:
    print("==============================")
    print("Patient Name:", patient.get_name())

    # Displays the patient type and billing information.
    patient.display_patient_type()

    print("Original Bill: ₱", format(patient.get_bill_amount(), ".2f"))
    print("Final Bill: ₱", format(patient.calculate_bill(), ".2f"))
