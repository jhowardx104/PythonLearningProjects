from random import randrange
from time import sleep
from prompts import *

diagnosis_list = []


def simulate_load():
    simulated_load = randrange(2, 5)
    sleep(simulated_load)


def assess_eyes(eyes):
    if eyes == '1':
        return no_dehydration
    elif eyes == '2':
        return severe_dehydration


def assess_skin(skin):
    if skin == '1':
        return some_dehydration
    elif skin == '2':
        return no_dehydration


def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == '1':
        eyes = input(eyes_prompt)
        return assess_eyes(eyes)
    elif appearance == '2':
        skin = input(skin_pinch_prompt)
        return assess_skin(skin)


def save_diagnosis(name, diagnosis):
    print('Saving diagnosis (%s) for patient %s...' % (diagnosis, name))
    simulate_load()
    diagnosis_list.append({'name': name, 'diagnosis': diagnosis})


def diagnose_new_patient():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_diagnosis(name, diagnosis)


def view_patient_history():
    print('Loading patient history...\n\n')
    simulate_load()
    print('Patient - Diagnosis')
    print('-------------------')
    for patient in diagnosis_list:
        print('%s - %s' % (patient['name'], patient['diagnosis']))
    print('\n\nPress any key to continue...')
    input()


def app_ready():
    print('Application ready.')
    while True:
        choice = input(action_prompt)
        if choice == '1':
            diagnose_new_patient()
        elif choice == '2':
            view_patient_history()
        elif choice == '3':
            return
        else:
            print(invalid_action_message)


def main():
    print(welcome_message)
    simulate_load()
    app_ready()


main()
