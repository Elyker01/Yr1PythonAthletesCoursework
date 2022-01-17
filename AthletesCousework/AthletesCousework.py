import csv
from collections import Counter
import time
import os

class Athletes:
    
    def __init__(self):
        pass
    

    def listNamesByLength(self):
        """Opens and reads the CSV file using the DictReader method, then creates an empty dictionary where for each column in the file,
           it will add the Name column as the key, and the NOC and Discipline columns as the value. After that,
           it creates another empty dictionary where the data is ordered by using the sorted method, using the length as the key. """

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
           #Use a for loop in order to arrange the keys in order of length by using the sorted method

        print('\n' * 2)

        AthletesList.close()

        
    def listTopFiveCountries(self):
        """ Opens and reads the CSV file using the DictReader method, then creates an empty list for the column NOC and appends the data in
            the column, to the NOC list. Uses the dict subclass 'Counter' in order to list the most common NOC's in the list and uses it in the sorted
            method in order to print the NOC's in alphabetical order, in case two or more countries have the same number of Athletes. """
        
        AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file

        NOC = []
        for column in file:
            NOC.append(column["NOC"]) #Add the data in the NOC section of the CSV to the NOC list

        print ("The top five countries with the highest number of athletes are : ", '\n')
        print(*sorted(Counter(NOC).most_common(5), key=lambda x: (-x[1], x[0])), sep = '\n') #Use counter in order to count the most common values for the NOC, with their respective number of athletes.
        print ('\n' * 2)

        AthletesList.close()
        
                
        #This will then sort the count descending and then will sort by name ascending in case there is NOC's with the same number of athletes.

    def listTopDiscipline(self):
        """ Opens and reads the CSV file using the DictReader method and creates lists for the 5 countries with the highest number of athletes for the NOC
            and the Discipline, in order to avoid lists being overwritten. For each column in the file, it will filter through it to find all the cells that
            contain the names of the top 5 NOC's. It will then append the cells that contain the data for the respective NOC's and adds them to the respective lists.
            Lastly, for each NOC, it will use the dict subclass Counter in order to find the most common Discipline for each NOC, and uses that inside the
            sorted method in order to sort for alphabetical order, in case disciplines have the same number of NOC's. """
        
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

        #Empty lists are created for all the top 5 countries so that they don't get overwritten.


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
        #For loop which will append the NOC and Discipline column to the respective empty list for the country by using if statements to filter
        
        print("The top discipline in the United States of America is : ")
        print(*sorted(Counter(disciplineUSA).most_common(1), key=lambda x: (-x[1], x[0])), sep = '\n') #Using sorted method and counter in order to find the most common sport in the USA's discipline list and also ordering it by alphabetical order in case there is a sport with the same number of athletes.
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
#Print statements to start off the program and show the user what they need to type once prompted

while True: #While loop in order to wait until a condition is met which is correct user input
    print('\n')
    choice = input("Please type in your option -> ")
    time.sleep(2)
    if choice.upper() == 'NAMES' or choice.lower() == 'names': #User input validation
        print('\n')
        Adelekan.listNamesByLength() 
        time.sleep(2)
        while True: #Nested while loop to check if user wants to find out more information e.g run the code above
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                time.sleep(1)
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"): 
                print('\n')
                time.sleep(1)
                print("Thank you for visiting this database!")
                os._exit(1)
                
                
                

            elif continueOption.lower() not in( "y","yes") or continueOption.lower() not in ("n", "no"): #User input validation
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
                print('\n')
                time.sleep(1)
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
                time.sleep(1)
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
    #If the user inputs an invalid word, then it will loop back to the first while loop where the input begins. This is done in order to avoid the code breaking when incorrect input has been put in.

        




#Adelekan.listNamesByLength()     
#Adelekan.listTopFiveCountries()
#Adelekan.listTopDiscipline()



