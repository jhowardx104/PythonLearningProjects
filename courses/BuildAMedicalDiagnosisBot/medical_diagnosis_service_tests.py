import unittest
from medical_diagnosis_service import MedicalDiagnosisService
import time


class MedicalDiagnosisServiceTests(unittest.TestCase):
    uat = MedicalDiagnosisService()

    def test_simulate_load(self):
        start = time.perf_counter()
        MedicalDiagnosisService.simulate_load()
        end = time.perf_counter()
        diff = end - start
        result = 2.0 <= diff <= 5.0
        self.assertTrue(result)

    def test_assess_eyes_given_1(self):
        result = MedicalDiagnosisService.assess_eyes('1')
        self.assertEqual(result, 'No dehydration')

    def test_assess_eyes_given_2(self):
        result = MedicalDiagnosisService.assess_eyes('2')
        self.assertEqual(result, 'Severe dehydration')

    def test_assess_skin_given_1(self):
        result = MedicalDiagnosisService.assess_skin('1')
        self.assertEqual(result, 'Some dehydration')

    def test_assess_skin_given_2(self):
        result = MedicalDiagnosisService.assess_skin('2')
        self.assertEqual(result, 'No dehydration')

    if __name__ == '__main__':
        unittest.main()