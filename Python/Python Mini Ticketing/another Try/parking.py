numOfCars = 0
def parkingPass(parkingPass):
    
 
    parkPass = 0
    
    while parkPass != True or parkPass != False:
            if parkingPass == "Y" or parkingPass == "y":

                parkPass = True

                passPrintAnswer = input("Do you need a parking pass? Y / N : ")
                passPrint = 0
                while passPrint != True or passPrint != False:
                   if passPrintAnswer == "Y" or passPrintAnswer == "y":
                        
                        
                        while True:
                            try:
                                global numOfCars
                                numOfCars = int(input("How many parking pass? : "))
                            except ValueError:
                                print("Please enter a number. :")
                            else:
                                break
                         
            
                        passPrint = True
                        break
                    
                   elif passPrintAnswer == "N" or passPrintAnswer == "n":
                        passPrint == False
                        break
                 
                   else:
                        passPrintAnswer = input("Enter your choice by Y/N : ")
                break
            elif parkingPass == "N" or parkingPass == "n":
                parkPass = False
          
                # print("Doesn't Need a Parking Pass")
             
                break
            else:
                parkingPass = input("Enter your choice by Y/N : ")
  




def parkingCars(numOfCars):
    print(f"\n\n\n---------------------------------------\n\t|  {numOfCars} parking pass |\n---------------------------------------\n\n")


# numOfcars = parkingPass()
    

# parkingPass()




