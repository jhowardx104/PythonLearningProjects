from random import randrange
from time import sleep
from prompts import *


class MedicalDiagnosisService:
    diagnosis_list = []

    def __init__(self):
        self.simulate_load()
        self.service_ready()

    @staticmethod
    def simulate_load():
        simulated_load = randrange(2, 5)
        sleep(simulated_load)

    @staticmethod
    def assess_eyes(eyes):
        if eyes == '1':
            return no_dehydration
        elif eyes == '2':
            return severe_dehydration

    @staticmethod
    def assess_skin(skin):
        if skin == '1':
            return some_dehydration
        elif skin == '2':
            return no_dehydration

    def assess_appearance(self):
        appearance = input(appearance_prompt)
        if appearance == '1':
            eyes = input(eyes_prompt)
            return self.assess_eyes(eyes)
        elif appearance == '2':
            skin = input(skin_pinch_prompt)
            return self.assess_skin(skin)

    def save_diagnosis(self, name, diagnosis):
        print('Saving diagnosis (%s) for patient %s...' % (diagnosis, name))
        self.simulate_load()
        self.diagnosis_list.append({'name': name, 'diagnosis': diagnosis})

    def diagnose_new_patient(self):
        name = input(name_prompt)
        diagnosis = self.assess_appearance()
        self.save_diagnosis(name, diagnosis)

    def view_patient_history(self):
        print('Loading patient history...\n\n')
        self.simulate_load()
        print('Patient - Diagnosis')
        print('-------------------')
        for patient in self.diagnosis_list:
            print('%s - %s' % (patient['name'], patient['diagnosis']))
        print('\n\nPress any key to continue...')
        input()

    @staticmethod
    def service_ready():
        print('Service is ready.')

    def start_service(self):
        while True:
            choice = input(action_prompt)
            if choice == '1':
                self.diagnose_new_patient()
            elif choice == '2':
                self.view_patient_history()
            elif choice == '3':
                print(closing_application)
                self.simulate_load()
                return
            else:
                print(invalid_action_message)
