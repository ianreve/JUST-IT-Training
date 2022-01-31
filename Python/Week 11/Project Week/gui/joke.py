from click import command
from guizero import App, Text, TextBox, PushButton, ButtonGroup

def jokes():
    if jokeChoice.value == "Stick":
        displayJoke.value = "What is brown and sticky?..............A Stick"

    # complete the code  by adding elif and else until you matche all the items in the list 




app = App(title="Joke App")

instruction = Text(app, text="Select a Joke from the list below")
jokeChoice = ButtonGroup(app, options=["Stick", "Fluff", "Chicken", "Frog"], selected="Stick")
btnJoke = PushButton(app, command=jokes,text="Show Jokes")
displayJoke = Text(app, text="Joke loading.............")


app.display()