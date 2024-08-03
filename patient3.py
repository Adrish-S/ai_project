import csv
import pandas as pd   
with open("symptoms_data.csv",'r') as file: 
    reader= csv.reader(file)
    next(reader)
    # print(reader)
    i = 0
    table_row = []
    for row in reader: 
        table_row.append(row) 

    for i in range(1,12):
        for j in range (1,15):
            table_row[i][j] = int(table_row[i][j])
            # print(table_row[i][j])
    symptoms = []
    print("\nfever:")
    fever = int(input())
    print("\ncough")
    cough= int(input())
    print("\nfatigue:")	
    Fatigue	= int(input())
    print("\nheadache:")	
    Headache	= int(input())
    print("\nnausea:")	
    Nausea	= int(input())
    print("\ndizziniess:")	
    Dizziness	= int(input())
    print("\njointpain:")	
    JointPain	= int(input())
    print("\nrash:")	
    Rash	= int(input())
    print("\nbreathshortness:")	
    Breath	= int(input())
    print("\nchestpain:")	
    ChestPain	= int(input())
    print("\nabdominalpain:")	
    AbdominalPain	= int(input())
    print("\nvomiting:")	
    Vomiting	= int(input())
    print("\ndiarrhea:")	
    Diarrhea= int(input())
    symptoms = [0,fever,cough,Fatigue,Headache,Nausea,Dizziness,JointPain,Rash,Breath,ChestPain,AbdominalPain,Vomiting,Diarrhea]
    disease_list = []
    for i in range(1,11):
        probablity = 1
        # probablity = (table_row[i][14]/table_row[11][14])(table_row[i][1]/table_row[i][14])
        probablity = (table_row[i][14]/table_row[11][14])
        for j in range(1,14):
            if (symptoms[j]):
                probablity = probablity*(table_row[i][j]/table_row[i][14])
            else:
                probablity = probablity*((table_row[i][14]-table_row[i][j])/table_row[i][14])
        disease_list.append(probablity*1000000000000)

    final_sum = 0
    print(symptoms)
    # print(disease_list)
    for g in range(0,len(disease_list)):
        final_sum = final_sum + disease_list[g]
    # final_sum = sum(disease_list)
    for k in range(0,len(disease_list)):
        disease_list[k] = disease_list[k]*100/final_sum
    print(disease_list)
    index = max(disease_list)
    # print(table_row[11][14])
    print("are you diagnosed : ")
    diagnosed = int(input())
    if (diagnosed):
        table_row[disease_list.index(index)+1] = table_row[disease_list.index(index)+1] + symptoms
    else:
        print("\nFurther Lab test for more precise sysmptoms needed")
        print("\nDid you had a new disease")
        new = int(input())
        if new :
            print("\nThe authorities will be notified and The samples will be sent to lab for risk assessment")
            
            
            ##get copyright and prepare an app for getting published ##choose category of disease ## chnage the symptom , train and get the new model according to the new dataset given by sir 
