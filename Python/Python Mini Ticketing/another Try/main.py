import time
import total
import printValues
import parking
# import 



printValues.welcome()
time.sleep(3)
printValues.ticketsPrices()



numOfAdults = int(input("\nHow many Adult tickets? : "))
numOfChild = int(input("How many Child tickets? : "))
numOfSenCitizen = int(input("How many Senior Citizen tickets? : "))
customerSurname = input("Enter your Surname : ")
parkingPass = input("Do you need a parking? Y / N:  ")
parking.parkingPass(parkingPass)


# numOfCars = parking.numOfCars()

def delay():
    total.totalPrices(numOfAdults, numOfChild, numOfSenCitizen)



customerOrder  = (total.totalPrices(numOfAdults,numOfChild,numOfSenCitizen))
printValues.reciept(customerSurname, numOfAdults, numOfChild, numOfSenCitizen, customerOrder[0], customerOrder[1], customerOrder[2]) 
# print((customerOrder[0]))

if parking.numOfCars != 0:
    parking.parkingCars(parking.numOfCars)
# numOfCard = parking.parkingPass()

printValues.ThankYou()




