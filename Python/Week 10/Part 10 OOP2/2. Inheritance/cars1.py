''' Inheritance is the process of defining a new object with the help of an existing object
 Two inheritance key principles are as follows
 1. Accessing existing objects functionality 
 2. Updating existing objects functionality
 Two other key terms are as follows
 1. Re-Usability and 2. IS-A Relation'''


class Cars: # create a super/parent class
    def __init__(self, model, year):
        self.cModel = model
        self.cYear = year

    def startCar(self): # create a method that starts the car
        print("Starting Car")
# create a child/sub class without the super method 
# class BMW(Cars):
#     def __init__(self,cruiseCenabled, model, year): # inherit attributes from the superclass
#         Cars.__init__(self,model,year,)
        
#         self.ccEnabled = cruiseCenabled

        
# bmwCar = BMW(True,"BMW","312E",2017)
# bmwCar.startCar()

# print(f"\nI am driving a {bmwCar.cYear} {bmwCar.cMake}, model {bmwCar.cModel}, with cruised control enabled = {bmwCar.ccEnabled}")

class Tesla(Cars):
  def __init__(self, model, year,selfDrive , make):
      super().__init__( model, year)
      self.sDrive = selfDrive
      self.cMake = make


teslaCar = Tesla("S",2020,True,"TESLA")
teslaCar.startCar()
print(f"\nI am driving a {teslaCar.cYear} {teslaCar.cMake}, model {teslaCar.cModel}, with self driving enabled = {teslaCar.sDrive}")
