from random import randrange
from time import sleep
from prompts import *

diagnosis_list = []


def simulate_load():
    simulated_load = randrange(2, 5)
    sleep(simulated_load)


def diagnose_new_patient():
    name = input(name_prompt)
    print("Diagnosing new")


def view_patient_history():
    print("Showing it all")


def app_ready():
    print('Application ready.')
    while(True):
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
