import csv
from collections import Counter
import time
import os

class Athletes:
    
    def __init__(self):
        pass
    

    def listNamesByLength(self):
        
        AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file

        dictAthletes = dict() #Create dictionary to store CSV sections
        for column in file:
            key = column["Name"]
            value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
            dictAthletes[key]= value

            #Iterate through the CSV file and set the column Name as the key, and the NOC and Discipline as the values.

        orderedDict = {}
        for k in sorted(dictAthletes, key = len):
           orderedDict[k] = dictAthletes[k]
           print(k, orderedDict[k])

        print('\n' * 2)

        AthletesList.close()

        
    def listTopFiveCountries(self):

        AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file

        NOC = []
        for column in file:
            NOC.append(column["NOC"]) #Add the data in the NOC section of the CSV to the NOC list

        print ("The top five countries with the highest number of athletes are : ", '\n')
        print(*sorted(Counter(NOC).most_common(5), key=lambda x: (-x[1], x[0])), sep = '\n')
        print ('\n' * 2)

        AthletesList.close()
        

        
        #This will then sort the count descending and then will sort by name ascending in case there is NOC's with the same number of athletes.

    def listTopDiscipline(self):

        AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file

        nocUSA = []
        disciplineUSA = []

        nocJapan = []
        disciplineJapan = []

        nocAustralia = []
        disciplineAustralia = []

        nocChina = []
        disciplineChina = []

        nocGermany = []
        disciplineGermany = []


        for column in file:
            if "United States of America" in column["NOC"]:
                nocUSA.append(column["NOC"])
                disciplineUSA.append(column["Discipline"])
            if "Japan" in column["NOC"]:
                nocJapan.append(column["NOC"])
                disciplineJapan.append(column["Discipline"])
            if "Australia" in column["NOC"]:
                nocAustralia.append(column["NOC"])
                disciplineAustralia.append(column["Discipline"])
            if "China" in column["NOC"]:
                nocChina.append(column["NOC"])
                disciplineChina.append(column["Discipline"])
            if "Germany" in column["NOC"]:
                nocGermany.append(column["NOC"])
                disciplineGermany.append(column["Discipline"])
        
        print("The top discipline in the United States of America is : ")
        print(*sorted(Counter(disciplineUSA).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n')
        print('\n' * 2)

        print("The top discipline in Japan is : ")
        print(*sorted(Counter(disciplineJapan).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n')
        print('\n' * 2)

        print("The top discipline in Australia is : ")
        print(*sorted(Counter(disciplineAustralia).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n')
        print('\n' * 2)

        print("The top discipline in China is : ")
        print(*sorted(Counter(disciplineChina).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n')
        print('\n' * 2)

        print("The top discipline in Germany is : ")
        print(*sorted(Counter(disciplineGermany).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n')
        print('\n' * 2)

        AthletesList.close()



Adelekan = Athletes() #Create an object of class athletes

print("Hello and welcome to the Tokyo Olympics 2020 Database.", '\n')
time.sleep(2)
print("If you'd like to list the athletes by name length please type 'NAMES'", '\n')
time.sleep(2)
print("If you'd like to list the top five countries by number of athletes please type 'COUNTRIES'", '\n')
time.sleep(2)
print("If you'd like to list the top discipline for the top five countries please type length please type 'DISCIPLINES'", '\n')
time.sleep(2)

while True:
    print('\n')
    choice = input("Please type in your option -> ")
    time.sleep(2)
    if choice.upper() == 'NAMES' or choice.lower() == 'names':
        print('\n')
        Adelekan.listNamesByLength()
        time.sleep(2)
        while True:
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"):
                print('\n')
                print("Thank you for visiting this database!")
                os._exit(1)
                
                
                

            elif continueOption.lower() not in( "y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(0.5)
                print('\n')
                print("Invalid answer, please type Y or N")
            

               

    elif choice.upper() == 'COUNTRIES' or choice.lower() == 'countries':
        print('\n')
        Adelekan.listTopFiveCountries()
        time.sleep(2)
        while True:
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"):
                print('\n')
                print("Thank you for visiting this database!")
                os._exit(1)
                
                
                

            elif continueOption.lower() not in( "y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")

    elif choice.upper() == 'DISCIPLINES' or choice.lower() == 'disciplines':
        print('\n')
        Adelekan.listTopDiscipline()
        while True:
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"):
                print('\n')
                print("Thank you for visiting this database!")
                os._exit(1)
                
                
                

            elif continueOption.lower() not in( "y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")

    elif choice.upper() != "NAMES" or "COUNTRIES" or "DISCIPLINES" or choice.lower() != "names" or "countries" or "disciplines":
        print('\n')
        print("Invalid Choice", '\n')
        time.sleep(0.5)
        print("Please retry. ")
        time.sleep(0.5)
        continue

        




#Adelekan.listNamesByLength()     
#Adelekan.listTopFiveCountries()
#Adelekan.listTopDiscipline()



