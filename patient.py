import csv

class SymptomChecker:
    def __init__(self, data_file):
        self.data_file = data_file
        self.symptoms = []
        self.table_row = []

    def load_data(self):
        with open(self.data_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.table_row.append([int(val) for val in row])

    def get_symptoms(self):
        print("\nEnter the severity of each symptom (0 for absent, 1 for mild, 2 for moderate, 3 for severe):")
        self.symptoms.append(0)  # Placeholder for index 0
        symptom_names = ["fever", "cough", "fatigue", "headache", "nausea", "dizziness", 
                         "joint pain", "rash", "shortness of breath", "chest pain", 
                         "abdominal pain", "vomiting", "diarrhea"]
        for symptom in symptom_names:
            severity = int(input(f"\n{symptom.capitalize()}: "))
            self.symptoms.append(severity)

    def calculate_probabilities(self):
        disease_list = []
        for i in range(1, 11):
            probability = self.table_row[i][14] / self.table_row[11][14]
            for j in range(1, 14):
                if self.symptoms[j]:
                    probability *= (self.table_row[i][j] / self.table_row[i][14])
                else:
                    probability *= ((self.table_row[i][14] - self.table_row[i][j]) / self.table_row[i][14])
            disease_list.append(probability * 1000000000000)

        final_sum = sum(disease_list)
        for k in range(len(disease_list)):
            disease_list[k] = disease_list[k] * 100 / final_sum
        return disease_list

    def diagnose(self):
        self.load_data()
        self.get_symptoms()
        disease_list = self.calculate_probabilities()
        max_index = disease_list.index(max(disease_list))
        print("Are you diagnosed with:")
        print(f"{self.table_row[max_index + 1][0]}?")

        diagnosed = input("Enter 1 if diagnosed, 0 otherwise: ")
        if diagnosed == '1':
            self.table_row[max_index + 1][1:] = [x + y for x, y in zip(self.table_row[max_index + 1][1:], self.symptoms[1:])]
        else:
            print("\nFurther lab tests for more precise symptoms needed.")
            new_disease = input("Did you have a new disease? Enter 1 if yes, 0 otherwise: ")
            if new_disease == '1':
                print("\nThe authorities will be notified and the samples will be sent to the lab for risk assessment.")

if __name__ == "__main__":
    checker = SymptomChecker("symptoms_data.csv")
    checker.diagnose()



# import pandas as pd
# from sklearn.naive_bayes import GaussianNB
# from sklearn.preprocessing import OneHotEncoder

# class SmartHospitalAgent:
#     def __init__(self):
#         self.symptom_data = None
#         self.disease_classifier = GaussianNB()

#     def load_data(self, file_path):
#         self.symptom_data = pd.read_csv(file_path)

#     def collect_symptoms(self):
#         if self.symptom_data is None:
#             raise ValueError("Symptom data not loaded. Please load data using load_data method.")
#         return self.symptom_data
    
#     def preprocess_data(self):
#         if self.symptom_data is None:
#             raise ValueError("Symptom data not loaded. Please load data using load_data method.")
#         encoded_data = pd.get_dummies(self.symptom_data.drop(columns=['Patient_ID', 'Disease']))
#         return encoded_data
    
#     def train_classifier(self, features, target):
#         self.disease_classifier.fit(features, target)

#     def predict_disease(self, symptoms):
#         if self.symptom_data is None:
#             raise ValueError("Symptom data not loaded. Please load data using load_data method.")
#         features = self.symptom_data.drop(columns=['Patient_ID', 'Disease'])
#         target = self.symptom_data['Disease']
#         encoded_symptoms = pd.get_dummies(pd.DataFrame([symptoms], columns=features.columns))
#         self.train_classifier(features, target)
#         prediction = self.disease_classifier.predict(encoded_symptoms)
#         return prediction[0]

#     def generate_patient_report(self):
#         if self.symptom_data is None:
#             raise ValueError("Symptom data not loaded. Please load data using load_data method.")
#         report = []
#         for index, row in self.symptom_data.iterrows():
#             patient_id = row['Patient_ID']
#             symptoms = row.drop(labels=['Patient_ID', 'Disease']).tolist()
#             predicted_disease = self.predict_disease(symptoms)
#             report.append({'Patient_ID': patient_id, 'Predicted_Disease': predicted_disease})
#         return pd.DataFrame(report)

# # Example usage
# if __name__ == "__main__":
#     agent = SmartHospitalAgent()
#     agent.load_data("symptom_data.csv")
#     encoded_data = agent.preprocess_data()
#     agent.load_data("symptom_data.csv")
#     report = agent.generate_patient_report()
#     print(report)
