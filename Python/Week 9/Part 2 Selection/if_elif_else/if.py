#Selection is used to control the flow of programs

from asyncio import TimerHandle
from traceback import print_tb


score = int(input('Enter the score: '))
#  more than 

if score > 29:
    print(f'Good score {score}')

if score < 29:
    print(f'Bad score {score}')

if score <= 28:
    print(f'Bad score {score}')

if score >= 29:
    print(f'Good score {score}')

if score != 29:
    print(f'score is {score}')
    
# exercise modify the program above using the opetators below 
# < 	less than
# > 	more than
# <= 	less than or equal to 
# >= 	greater than or equal to
# !=    Not equal to