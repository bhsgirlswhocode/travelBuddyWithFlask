# importing csv module
import csv
import math

def findMPG (make, model, year):

    # initializing the titles and rows list
    rows = []
    x = -1
    modelF = False
    yearF = False

    # reading csv file
    with open('/home/bhsgwc/mysite/templates/vehicles.csv', 'r') as csvfile:
    	# creating a csv reader object
    	csvreader = csv.reader(csvfile)

    	# extracting each data row one by one
    	for row in csvreader:
    		rows.append(row)


    	for row in rows:
    	    if row[46] == make and row[47] == model and row[63] == year:
    	        x = int(row[34])
    return x

#print(findMPG("Ferrari", "Testarossa", "1985"))

def findInfo ():
    capacity = 30
    mpg = 14
    dec = 0.75
    totalMiles = 383
    startingGal = capacity * dec
    tillFirstGas = startingGal * mpg
    totalGasStations = math.ceil((totalMiles - tillFirstGas) / (capacity * mpg))
    averagePerGas = 35
    totalMoneySpent = totalGasStations * averagePerGas

    return str("Total Miles: " + str(totalMiles) + "\n" + "Miles until Gas: " + str(tillFirstGas) + "\n" + "Money Spent: " + str(totalMoneySpent))




