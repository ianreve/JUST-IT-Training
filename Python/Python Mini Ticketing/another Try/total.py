
from pickletools import read_uint1


adult = 20
child = 12
seniorCitizen = 11





def totalPrices(numOfAdults, numOfChild, numOfSenCitizen):
    adultsTotal = numOfAdults * adult
    childTotal = numOfChild * child
    senCitizenTotal = numOfSenCitizen * seniorCitizen
    totalTicketPrice = adultsTotal+childTotal+senCitizenTotal
    
    return adultsTotal, childTotal, senCitizenTotal,totalTicketPrice


# def total(adultsTotal,childTotal,senCitizenTotal):
#     totalTicketPrice = adultsTotal+childTotal+senCitizenTotal
#     return totalTicketPrice
# price = total()


# print(totalPrices(numOfAdults,numOfChild,numOfSenCitizen))