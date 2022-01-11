import csv

class Athletes:
    



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


    def listByLength(self):
        
        dictAthletes = dict() #Create dictionary to store CSV sections
        for column in file:
            key = column["Name"]
            value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
            dictAthletes[key]= value

            #Iterate through the CSV file and set the column Name as the key, and the NOC and Discipline as the values.

        
        #Method to sort names in order of length
        #sortedNames = sorted(key, key=lambda x: -len(x), reverse=True) #Sort the names list in order of length
        #print(*sortedNames, sep = '\n') #Change the format of the list from vertical to horizontal

        orderedDict = {}
        for k in sorted(dictAthletes, key = len):
           orderedDict[k] = dictAthletes[k]
           print(k, orderedDict[k])

 
        



Adelekan = Athletes() #Create an object of class athletes
AthletesList = open('Athletes.csv', 'r') #Open Athletes.csv in read mode
file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file
Adelekan.listByLength()                                                        