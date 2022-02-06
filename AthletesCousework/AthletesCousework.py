import csv
from collections import Counter
import time
import os
import string


class Athletes:
    """ 
    Attributes
    ----------
    isCreated = bool
        boolean to check object state

    Methods
    ----------
    listNames(fileName)
    Lists shortest and longest names in the file.

    checkObjectState()
    Checks whether the object is created or not.

    listNamesByLength(fileName)
    Lists all the names in the file, according to length and alphabetical order.

    listTopFiveCountries(fileName)
    Lists the top 5 countries with the highest number of athletes.

    listTopDiscipline(fileName)
    For the top 5 countries, it lists the top disciplines for each one.



        """
    
    def __init__(self):
        """ 
        Constructor that creates an object of class Athletes
        and contains a boolean variable named isCreated which is used
        in order to check whether the object has been created successfully.

       """

        isCreated = True
        
    def __del__(self):
        """ 
        Destructor that deletes object of class Athletes

        """
    
    def listNames(self, fileName):

        """Opens and reads the CSV file using the DictReader method,
           then creates an empty dictionary where for each column in the file,
           it will add the Name column as the key,
           and the NOC and Discipline columns as the value.
           After that, it creates another empty dictionary 
           where the data is sorted by the length of the names, 
           regardless of whitespace, fullstops or apostrophes. 

            Parameters
            ----------
            fileName : str
                Name of CSV file to be opened.

            Returns
            -------
            None
           
           Doctests will show the functionality where it creates a generator object, 
           and where it strips the full stops and whitespaces.

          >>> Adelekan = Athletes()
          >>> Adelekan.listNames('test.csv')
          Generator object of class Athletes created in memory

          >>> for k in Adelekan.listNames('test.csv'):
          ...   print(k)
          ('Ade', {'NOC': 'United States of America', 'Discipline': 'Cycling Road'})
          ('OBA', {'NOC': 'Japan', 'Discipline': 'Artistic Gymnastics'})
          ('ADELEKAN ADELEKAN ADELEKAN ADELEKAN ADELEKAN', {'NOC': 'Australia', 'Discipline': 'Rowing'})
          ('OBA OBA OBA OBA OBA OBA OBA ADELEKAN ELYKER ELYKER', {'NOC': 'China ', 'Discipline': 'Basketball'})

          



           """


        AthletesList = open(fileName, 'r') #Open Athletes.csv in read mode
        file = csv.DictReader(AthletesList) #Create an object containing the content in the csv file
        

        dictAthletes = dict() #Create dictionary to store CSV sections
        for column in file:
            column["Name"] = column["Name"].rstrip(".").rstrip() 
            #rstrip() method removes full stops and trailing whitespace
            key = column["Name"]
            value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
            dictAthletes[key]= value

        #Iterate through the CSV file and set the column Name as the key, 
        #and the NOC and Discipline as the values.


        orderedDict = {}
        for k in sorted(dictAthletes, key=lambda k: len(k.replace(' ', '').replace(".","").replace("'",""))):
            if len(k.replace(" ","").replace(".","").replace("'","")) < 5:    
                orderedDict[k] = dictAthletes[k]
                yield(k, orderedDict[k])
                #Generator is created here which is then iterated upon in main method

        #Use a for loop in order to arrange the keys in order of length
        #by using the sorted and the replace method, 
        #ignoring whitespace,full stops and apostrophes.
          
            if len(k.replace(" ","").replace(".","").replace("'","")) > 31:
                orderedDict[k] = dictAthletes[k]
                yield(k, orderedDict[k])

            
               

        print('\n' * 2)

        AthletesList.close()

        
        def checkObjectState(self):
            """ Method that checks whether object of class Athletes has been created 
            Parameters
            ----------
            None

            Returns
            -------
            isCreated
            """
            return isCreated
 
    def listNamesByLength(self, fileName):
        """Opens and reads the CSV file using the DictReader method,
           then creates an empty dictionary where for each column in the file,
           it will add the Name column as the key, 
           and the NOC and Discipline columns as the value. After that,
           it creates another empty dictionary where the data is ordered
           by using the sorted method, using the length(ignoring whitespace,
           fullstops and apostrophes) as the key.

            Parameters
            ----------
            fileName : str
                Name of CSV file to be opened.

            Returns
            -------
            None

          Open the test CSV file, and create a generator object of class Athletes.

          >>> Adelekan = Athletes()
          >>> Adelekan.listNamesByLength('test.csv')
          Generator object of class Athletes created in memory

          Iterate on the generator object and print out the names
          in order of name length.

          >>> for k in Adelekan.listNamesByLength('test.csv'):
          ...      print(k)
          ('Ade', {'NOC': 'United States of America', 'Discipline': 'Cycling Road'})
          ('OBA', {'NOC': 'Japan', 'Discipline': 'Artistic Gymnastics'})
          ('ELYKER', {'NOC': 'Germany', 'Discipline': 'Athletics'})
          ('KHAMISI', {'NOC': 'Japan', 'Discipline': 'Tennis'})
          ('SALTYSKILLS', {'NOC': 'United States of America', 'Discipline': 'Boxing'})
          ('ADELEKAN ADELEKAN ADELEKAN ADELEKAN ADELEKAN', {'NOC': 'Australia', 'Discipline': 'Rowing'})
          ('OBA OBA OBA OBA OBA OBA OBA ADELEKAN ELYKER ELYKER', {'NOC': 'China ', 'Discipline': 'Basketball'})

          """



        AthletesList = open(fileName, 'r') 
        file = csv.DictReader(AthletesList) 

        dictAthletes = dict() 
        for column in file:
            column["Name"] = column["Name"].rstrip(".").rstrip()
            key = column["Name"]
            value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
            dictAthletes[key]= value
   
            #Iterate through the CSV file and set the column Name as the key,
            #and the NOC and Discipline as the values.

        orderedDict = {}
        for k in sorted(dictAthletes, key=lambda k: len(k.replace(' ', '').replace(".","").replace("'",""))): 
        #Sorting the dictionary, ignoring whitespace, fullstops and apostrophes
               orderedDict[k] = dictAthletes[k] 
               yield(k, orderedDict[k])
           #Use a for loop in order to arrange the keys in order of length by using the sorted method

        print('\n' * 2)

        AthletesList.close()

    def listTopFiveCountries(self,fileName):
        """ Opens and reads the CSV file using the DictReader method,
            then creates an empty list for the column NOC and appends the data in
            the column, to the NOC list. Uses the dict subclass 'Counter' 
            in order to list the most common NOC's in the list and uses it in the sorted
            method in order to print the NOC's in alphabetical order, 
            in case two or more countries have the same number of Athletes.

            Parameters
            ----------
            fileName : str
                Name of CSV file to be opened.

            Returns
            -------
            None

            Open the test CSV file, and print out the countries with
            the highest number of athletes.

            >>> Adelekan = Athletes()
            >>> Adelekan.listTopFiveCountries('test.csv')
            ('Japan', 2)
            ('United States of America', 2)
            ('Australia', 1)
            ('China', 1)
            ('Germany', 1)


        """

        AthletesList = open(fileName, 'r') 
        file = csv.DictReader(AthletesList)

        NOC = []
        for column in file:
            NOC.append(column["NOC"]) 
            #Add the data in the NOC section of the CSV to the NOC list

        print ("The top five countries with the highest number of athletes are : ", '\n')
        print(*sorted(Counter(NOC).most_common(5),
                     key=lambda x: (-x[1], x[0])), sep = '\n') 
        #Use counter in order to count the most common values for the NOC,
        #with their respective number of athletes
        #and lambda function in order to sort it alphabetically, 
        #in case they have the same number of athletes .
        print ('\n' * 2)

        AthletesList.close()
        
                
        #This will then sort the count descending and then will sort by name ascending
        #in case there is NOC's with the same number of athletes.



    def listTopDiscipline(self,fileName):
        """ Opens and reads the CSV file using the DictReader method 
            and creates lists for the 5 countries
            with the highest number of athletes for the NOC and the Discipline.
            For each column in the file, it will filter through to find all the cells that
            contain the names of the top 5 NOC's.
            It will then append the cells that contain the data for the respective NOC's
            and adds them to the respective lists.
            Each NOC is identified using the most common method used in the NOC column
            and then the tuple is enumerated upon, assigning the countries in order
            of an index, with 0 being the highest country and 4 being the lowest.
            For each NOC, it will use the dict subclass Counter in order
            to find the most common Discipline for each NOC, and uses that inside the
            sorted method in order to sort for alphabetical order, 
            in case disciplines have the same number of NOC's. 

            Parameters
            ----------
            fileName : str
                Name of CSV file to be opened.

            Returns
            -------
            None

            Open the test CSV file and print out the most common discipline for each country
            that has the highest number of athletes.
            
            >>> Adelekan = Athletes()
            >>> Adelekan.listTopDiscipline('test.csv')
            The top discipline in the United States of America is :
            ('Cycling Road', 1)
            The top discipline in Japan is :
            ('Artistic Gymnastics', 1)
            The top discipline in Australia is :
            ('Rowing', 1)
            The top discipline in China is :
            ('Basketball', 1)
            The top discipline in Germany is :
            ('Athletics', 1)
            
            """
        
        AthletesList = open(fileName, 'r') 
        file = csv.DictReader(AthletesList)
        NOC = []
        nocFirst = []
        disciplineFirst = []

        nocSecond = []
        disciplineSecond = []

        nocThird = []
        disciplineThird = []

        nocFourth = []
        disciplineFourth = []

        nocFifth = []
        disciplineFifth = []

        for column in file:
            NOC.append(column["NOC"])
            nocCounter = Counter(NOC)
            topFiveCountries = nocCounter.most_common(5)
            for number,value in enumerate(topFiveCountries): 
                globals()[f'NOC{number + 1}'] = value

        AthletesList.seek(0) #Read file from the start again
        for column in file:
            if NOC1[0] in column["NOC"]:
                nocFirst.append(column["NOC"])
                disciplineFirst.append(column["Discipline"])
            elif NOC2[0] in column["NOC"]:
                nocSecond.append(column["NOC"])
                disciplineSecond.append(column["Discipline"])
            elif NOC3[0] in column["NOC"]:
                nocThird.append(column["NOC"])
                disciplineThird.append(column["Discipline"])
            elif NOC4[0] in column["NOC"]:
                nocFourth.append(column["NOC"])
                disciplineFourth.append(column["Discipline"])
            elif NOC5[0] in column["NOC"]:
                nocFifth.append(column["NOC"])
                disciplineFifth.append(column["Discipline"])

        #For loop which will append the NOC and Discipline column
        #to the respective empty list for the country
        #by using if statements to filter
        
        print("The top discipline in", NOC1[0], "is : "),
        print(*sorted(Counter(disciplineFirst).most_common(1), 
                      key=lambda x: (-x[1], x[0])), sep = '\n')

        print("The top discipline in", NOC2[0], "is : ")
        print(*sorted(Counter(disciplineSecond).most_common(1),
                     key=lambda x: (-x[1], x[0])), sep = '\n') 

        print("The top discipline in", NOC3[0], "is : ")
        print(*sorted(Counter(disciplineThird).most_common(1),
                     key=lambda x: (-x[1], x[0])), sep = '\n') 

        print("The top discipline in", NOC4[0], "is : ")
        print(*sorted(Counter(disciplineFourth).most_common(1),
                     key=lambda x: (-x[1], x[0])), sep = '\n') 

        print("The top discipline in", NOC5[0], "is : ")
        print(*sorted(Counter(disciplineFifth).most_common(1),
                     key=lambda x: (-x[1], x[0])), sep = '\n') 
        #Using sorted method and counter in order to find the most common sport
        #in the USA's discipline list
        #and also ordering it by alphabetical order,
        #in case there is a sport with the same number of athletes.

        AthletesList.close()



class AthletesChild(Athletes):
    """
    Attributes
    ----------
    isCreated = bool
        boolean to check object state

    Methods
    ----------
    listNames(fileName,shortest)
    Lists shortest names in the file.

    innerListNames(fileName,longest)
    Lists longest names in the file. (Function Decorator)

    checkObjectState()
    Checks whether the object is created or not.

    listNamesByLength(fileName)
    Lists all the names in the file, according to length and alphabetical order.

    listTopFiveCountries(fileName)
    Lists the top 5 countries with the highest number of athletes.

    listTopDiscipline(fileName)
    For the top 5 countries, it lists the top disciplines for each one.
    """

    def __init__(self):
        """ This constructor inherits the Athletes class variable and methods 
            which can be used in the child class and be overriden"""
        super().__init__()

    def listNames(self,fileName,shortest):
        """Opens and reads the CSV file using the DictReader method, 
           then creates an empty dictionary where for each column in the file,
           it will add the Name column as the key,
           and the NOC and Discipline columns as the value. 
           After that, it creates another empty dictionary 
           where the data is sorted by the length of the names, 
           regardless of whitespace, fullstops or apostrophes.
           This method has been overriden from the parent 'Athletes' class 
           into the AthletesChild class and takes a boolean parameter named shortest
           in order to differentiate from the parent method
           and choose between showing the shortest
           and longest names in the main method.

            Parameters
            ----------
            fileName : str
                Name of CSV file to be opened.
            
            shortest : bool
                if True, method will print the shortest names

            Returns
            -------
            None

           Open and read the test CSV file, and given the shortest parameter is True,
           print out the shortest names in the CSV file.

           >>> AdelekanChild = AthletesChild()
           >>> AdelekanChild.listNames('test.csv',True)
           Ade, {'NOC': 'Norway', 'Discipline': 'Cycling Road'}
           OBA, {'NOC': 'Spain', 'Discipline': 'Artistic Gymnastics'}
          
          """

        if shortest == True:
            AthletesList = open(fileName, 'r') 
            file = csv.DictReader(AthletesList) 
        

            dictAthletes = dict()
            for column in file:
                column["Name"] = column["Name"].rstrip(".").rstrip()
                key = column["Name"]
                value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
                dictAthletes[key]= value


            orderedDict = {}
            for k in sorted(dictAthletes, key=lambda k: 
                            len(k.replace(' ', '').replace(".","").replace("'",""))):
                if len(k.replace(" ","").replace(".","").replace("'","")) < 5:
                    orderedDict[k] = dictAthletes[k]
                    print(k, orderedDict[k])
        
        
            print('\n' * 2)
            AthletesList.close()

        def innerListNames(fileName,longest):
            """ Inner function here with a decorator in the main function 
                which is then called when the user inputs 'long' when prompted. 
                It opens the CSV file and creates an empty dict.
                It then appends each column and adds it to the key/value.
                Lastly, it prints out all the keys and values where the name is longer than
                31 characters (ignoring whitespace, fullstops and apostrophes).

                Parameters
                ----------
                fileName : str
                    Name of CSV file to be opened.
            
                longest : bool
                    if False, method will print the longest names

                Returns
                -------
                innerListNames
                """

            if longest == False:
                AthletesList = open(fileName, 'r') 
                file = csv.DictReader(AthletesList) 
        

                dictAthletes = dict() 
                for column in file:
                    column["Name"] = column["Name"].rstrip(".").rstrip()
                    key = column["Name"]
                    value = {"NOC": column["NOC"], "Discipline": column["Discipline"]}
                    dictAthletes[key]= value


                orderedDict = {}
                for k in sorted(dictAthletes, key=lambda k:
                               len(k.replace(' ', '').replace(".","").replace("'",""))):
                    if len(k.replace(" ","").replace(".","").replace("'","")) > 31:
                        orderedDict[k] = dictAthletes[k]
                        print(k, orderedDict[k])
            print('\n' * 2)
            AthletesList.close()
        return innerListNames

                #Use a for loop in order to arrange the keys in order of length
                #by using the sorted and the replace method, 
                #ignoring whitespace,full stops and apostrophes.
        
        
        print('\n' * 2)
        AthletesList.close()

    






    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

Adelekan = Athletes() #Create an object of class athletes
AdelekanChild = AthletesChild() # Create an object of child class

print("----------------------------------------------------------------------")
print("\n")
print("Hello and welcome to the Tokyo Olympics 2020 Database.", '\n')
time.sleep(2)
print("If you'd like to list the shortest and longest athlete names please type 'NAMES'", '\n')
time.sleep(2)
print("If you'd like to list only the shortest athlete names please type 'SHORT'", '\n')
time.sleep(2)
print("If you'd like to list only the longest athlete names please type 'LONG'", '\n')
time.sleep(2)
print("If you'd like to list all the athletes name from shortest to longest please type 'ALL NAMES'", '\n')
time.sleep(2)
print("If you'd like to list the top five countries by number of athletes please type 'COUNTRIES'", '\n')
time.sleep(2)
print("If you'd like to list the top discipline for the top five countries please type length please type 'DISCIPLINES'", '\n')
time.sleep(2)

#Print statements to start off the program and show the user what they need to type once prompted



while True: 
    #While loop in order to wait until a condition is met which is correct user input
    print('\n')
    choice = input("Please type in your option -> ") 
    #User input
    time.sleep(2)
    if choice.upper() == 'NAMES' or choice.lower() == 'names': 
        #User input validation
        print('\n')
        for k in Adelekan.listNames('Athletes.csv'):
            print(k)
        time.sleep(2)

        while True: 
            #Nested while loop to check if user wants to find out more information e.g run the code above
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                time.sleep(1)
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"): 
                print('\n')
                time.sleep(1)
                print("Thank you for vising this database!")
                del Adelekan
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"): 
                time.sleep(0.5)
                print('\n')
                print("Invalid answer, please type Y or N")
            

               
    elif choice.upper() == 'SHORT' or choice.lower() == 'short': 
        #Elif statements for each user choice
        print('\n')
        AdelekanChild.listNames('Athletes.csv',True)
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
                print("Thank you for vising this database!")
                del AdelekanChild
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")



    elif choice.upper() == 'LONG' or choice.lower() == 'long':
        print('\n')
        listLongest = AdelekanChild.listNames('Athletes.csv',False) 
        #Function decorator here which calls on the inner function
        listLongest('Athletes.csv',False)
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
                print("Thank you for vising this database!")
                del AdelekanChild
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")



    elif choice.upper() == 'ALL NAMES' or choice.lower() == 'all names':
        print('\n')
        for k in Adelekan.listNamesByLength('Athletes.csv'): 
            #Generator that is created in that function is now iterated upon, and prints out the dictionary
            print(k)
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
                print("Thank you for vising this database!")
                del Adelekan
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")



    elif choice.upper() == 'COUNTRIES' or choice.lower() == 'countries':
        print('\n')
        Adelekan.listTopFiveCountries('Athletes.csv')
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
                print("Thank you for vising this database!")
                del Adelekan
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"):
                time.sleep(1)
                print('\n')
                print("Invalid answer, please type Y or N")



    elif choice.upper() == 'DISCIPLINES' or choice.lower() == 'disciplines':
        print('\n')
        print("Please wait...")
        print("\n")
        Adelekan.listTopDiscipline('Athletes.csv')
        time.sleep(1)
        while True:
            continueOption = input("Would you like to find out more information? Y/N  " '\n')
            if continueOption.lower() in ("y", "yes"):
                time.sleep(1)
                print ("Great! " '\n')
                time.sleep(1)
                break
                
            elif continueOption.lower() in ("n", "no"):
                print('\n')
                print("Thank you for vising this database!")
                del Adelekan
                print('\n')
                os._exit(1)

            elif continueOption.lower() not in("y","yes") or continueOption.lower() not in ("n", "no"):
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
    
    #If the user inputs an invalid word, then it will loop back to the first while loop where the input begins.
    # This is done in order to avoid the code breaking when incorrect input has been put in.

        






