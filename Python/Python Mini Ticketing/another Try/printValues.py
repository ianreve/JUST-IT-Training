from total import adult, child, seniorCitizen 
from datetime import date 

def welcome():
  
    print("\n\n---------------------------------------\n   Welcome to Adventure Theme Park\n---------------------------------------\n\n\n")
def ticketsPrices():
    
    print(f"        Entrance Ticket Prices    \n---------------------------------------\n\n \tAdult -------------- £{adult}\n\tChild -------------- £{child}\n\tSenior citizen ----- £{seniorCitizen}\n\n---------------------------------------")


def reciept(customerSurname,  numOfAdults, numOfChild, numOfSenCitizen, adultsTicketsTotal, childsTicketsTotal, senCitizenTicketsTotal ):

    today = date.today()
    print(f"\n---------------------------------------\n\n \t\t{today}\n\n\t   Customer: {customerSurname}\n \n \tAdult -------------{numOfAdults} = £{adultsTicketsTotal}\n\tChild -------------{numOfChild} = £{childsTicketsTotal}\n\tSenior citizen ----{numOfSenCitizen} = £{senCitizenTicketsTotal}\n\n\t\tTotal is £{adultsTicketsTotal + childsTicketsTotal + senCitizenTicketsTotal}\n\n---------------------------------------")  

# def recieptWithPass(customerSurname,  numOfAdults, numOfChild, numOfSenCitizen, adultsTicketsTotal, childsTicketsTotal, senCitizenTicketsTotal):
    
#     today = date.today()
#     print(f"\n---------------------------------------\n\n \t\t{today}\n\n\t   Customer: {customerSurname}\n \n \tAdult ------------{numOfAdults} = £{adultsTicketsTotal}\n\tChild -------------{numOfChild} = £{childsTicketsTotal}\n\tSenior citizen ----{numOfSenCitizen} = £{senCitizenTicketsTotal}\n\n\t\tTotal is £{adultsTicketsTotal + childsTicketsTotal + senCitizenTicketsTotal}\n\n---------------------------------------")  
#     # print(f"---------------------------------------\n {numOfCars} car(s) parking pass attached\n---------------------------------------")

def ThankYou():
    print("\n---------------------------------------\n    Thank You for Your Purchase :)\n---------------------------------------")
# welcome()

# ticketsPrices()

