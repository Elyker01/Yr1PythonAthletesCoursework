import csv

class Athletes:


    def openAthletes(self):
        
        with open('Athletes.csv', 'r',) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)


           




Adelekan = Athletes()
Adelekan.openAthletes()