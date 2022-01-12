import csv
from collections import Counter

class Athletes:
    

    def listByLength(self):
        
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
 
        
    def listTopFive(self):

        AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file

        NOC = []
        for column in file:
            NOC.append(column["NOC"]) #Add the data in the NOC section of the CSV to the NOC list
        print ("The top five countries with the highest number of athletes are : ")
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
        
        print("The top discipline in America is : ")
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
Adelekan.listByLength()         
Adelekan.listTopFive()
Adelekan.listTopDiscipline()



