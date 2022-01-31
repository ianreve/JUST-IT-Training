from guizero import App, Text, TextBox, PushButton

app = App(title="Adding Numbers", bg="cadetblue" )

instruction1 = Text(app, text=" Enter first number")
txtbox1 = TextBox(app)

instruction1 = Text(app, text=" Enter second number")
txtbox2 = TextBox(app)

txtAnswer = Text(app, text="Answer will be displayed here", color="red", bg="white")

def addNums():
    # create two local variabes 
    num1 = txtbox1.value # use ,value to capture input entered in the textboxes
    num2 = txtbox2.value

    total = int(num1) +  int(num2)
    txtAnswer.value = total



addButton = PushButton(app, command=addNums, text="Add")


app.display()