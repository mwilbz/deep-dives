import fhirclient.models.patient as patient_model
import json

if __name__ == '__main__':
	patient_json = json.load(open('patient.json'))
	patient = patient_model.Patient(patient_json)
