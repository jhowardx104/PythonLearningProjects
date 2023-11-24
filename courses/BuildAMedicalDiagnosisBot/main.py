from prompts import welcome_message
from medical_diagnosis_service import MedicalDiagnosisService

def main():
    print(welcome_message)
    medical_diagnosis_bot = MedicalDiagnosisService()
    medical_diagnosis_bot.start_service()


main()
