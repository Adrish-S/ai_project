import csv

class SmartHospitalAgent:
    def __init__(self):
        self.symptoms_data = {}
        self.disease_database = {
            "Common Cold": ["Runny nose", "Sneezing", "Cough", "Sore throat", "Fever"],
            "Influenza": ["Fever", "Body aches", "Headache", "Fatigue", "Cough"],
            # Add more diseases and their associated symptoms as needed
        }

    def collect_symptoms(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                patient_id, symptoms = row[0], row[1:]
                self.symptoms_data[patient_id] = symptoms
                print(symptoms)

    def detect_disease(self, patient_id):
        if patient_id not in self.symptoms_data:
            return "Patient ID not found"

        symptoms = self.symptoms_data[patient_id]
        for disease, symptoms_list in self.disease_database.items():
            if all(symptom == "Yes" for symptom in symptoms_list):
                return disease

        return "No disease detected"

    def generate_report(self):
        report = {}
        for patient_id in self.symptoms_data:
            disease = self.detect_disease(patient_id)
            report[patient_id] = disease
        return report

# Example usage
if __name__ == "__main__":
    agent = SmartHospitalAgent()
    agent.collect_symptoms("symptoms_data.csv")
    report = agent.generate_report()
    for patient_id, disease in report.items():
        print(f"Patient ID: {patient_id}, Disease Detected: {disease}")

