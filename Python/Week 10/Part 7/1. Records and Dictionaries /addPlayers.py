
players = []

add_players = True
while add_players:
    userName = input("Enter Username: ")
    password= input("Enter Password: ")
    score = int(input("Enter Score: "))
    highestScore = int(input("Enter Highest Score: "))

    player = {"user": userName,
    "pass":password,
    "Uscore":score,
    "hScore":highestScore

    }

    players.append(player)

    answer = input("Would you like to add another player Y/N:").upper()
    if answer == "N":
        add_players=False

print(players)

# print(players["user", "pass"])

aRecord = int(input("Enter the number of record you want to display: "))
aPlayer = (players[aRecord])

playerAtrribute = input("Which attribute would you like to print :")
print(aPlayer[playerAtrribute])

