'''
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2 with same apportch human ne kiya hai esa lagna chaiye ek learner approch se krna 

'''
from collections import namedtuple

patient = namedtuple("Patient", ["patient_id", "patient_name", "age", "disease"])

n = int(input("Enter number of patients: "))

patients = []

# 1. Read patient records
for i in range(n):
    patient_id, patient_name, age, disease = input().split()

    p = patient(patient_id, patient_name, int(age), disease)
    patients.append(p)


# 2. Display all patient details
print("\nAll Patients:")

for p in patients:
    print(p.patient_id, p.patient_name, p.age, p.disease)


# 3. Display patients whose age is above 60
print("\nPatients Above 60:")

for p in patients:
    if p.age > 60:
        print(p.patient_id, p.patient_name, p.age, p.disease)


# 4. Search patient using Patient ID
search_id = input("\nEnter Patient ID: ")

for p in patients:
    if p.patient_id == search_id:
        print("\nPatient Found:")
        print(p.patient_id, p.patient_name, p.age, p.disease)


# 5. Count patients suffering from a particular disease
search_disease = input("Enter Disease: ")

count = 0

for p in patients:
    if p.disease == search_disease:
        count += 1

print("\nPatients with", search_disease + ":")
print(count)