from cgitb import text
from guizero import App, Text  #import guizero library/module and specific classes

# create an instance object 
helloApp = App()

# create an instance object  with variable hello from the Text class and use it text property and assign it a value 
hello = Text(helloApp, text="Hello Python Gui") 

helloApp.display() # invoke/call the diplay method to return a GUI window