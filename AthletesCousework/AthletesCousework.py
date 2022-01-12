import csv
from collections import Counter

class Athletes:
    

    def listByLength(self):
        
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

 
        
    def listTopFive(self):
        dictAthletes = dict() #Create dictionary to store CSV sections
        NOC = []
        for column in file:
            NOC.append(column["NOC"]) #Add the data in the NOC section of the CSV to the NOC list

        count = Counter(NOC)
        print(*sorted(Counter(NOC).most_common(5), key=lambda x: (-x[1], x[0])), sep = '\n')
        #This will then sort the count descending and then will sort by name ascending in case there is NOC's with the same number of athletes.

    def listTopDiscipline(self):
        dictAthletes = dict()
        for column in file:
            key = column["NOC"]
            value = {"Discipline": column["Discipline"]}
            dictAthletes[key]= value






Adelekan = Athletes() #Create an object of class athletes
AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file
#Adelekan.listByLength()         
#Adelekan.listTopFive()
Adelekan.listTopDiscipline()








#Method to sort names in order of length
#sortedNames = sorted(key, key=lambda x: -len(x), reverse=True) #Sort the names list in order of length
#print(*sortedNames, sep = '\n') #Change the format of the list from vertical to horizontal

#def openAthletes(self):
        
        #with open('Athletes.csv', 'r',) as file:
            #reader = csv.reader(file)
            #for row in reader:
             #   nameColumn.append(row[0])
            #for item in nameColumn:
             #   print(item)

    #def openAthletes2(self):
       # filename = open('Athletes.csv', 'r')
        #file = csv.DictReader(filename)
