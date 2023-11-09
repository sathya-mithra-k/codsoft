#instructuion for user
print("WELCOME TO THE ROCK, PAPER AND SCISSOR GAME\n----------------------------------------------\nGame rules:\n 1. The user should choose rock, paper or scissor\n 2. rock beats scissors, paper beats rock and scissor beats paper\n  GOOD LUCK WITH THE GAME!!!!!! ")

#importing random to generate from computer's move
import random

#number of games won by user
user_wins =  0
#number of games won by computer 
computer_wins = 0
while True:
#creating a list of moves to generate random moves
    moves = ["rock", "paper", "scissor"]
#generating the computer's move
    computer_move = random.choice(moves)
#getting input from user
    user_input = input("choose rock, paper or scissor: ")
#checking the  game condition to see who won
    if user_input == computer_move:
        print(f"Your choice: {user_input}\nComputer's choice {computer_move}")
        print("TIE")
    elif (user_input == 'rock' and computer_move == "paper") or (user_input == 'paper' and computer_move == 'scissor') or (user_input == "scissor" and computer_move == 'rock'):
        print(f"Your choice: {user_input}\nComputer's choice {computer_move}")
        print("OOPS....YOU LOST!!!")
        computer_wins += 1
    else:
        print(f"Your choice: {user_input}\nComputer's choice {computer_move}")
        print("CONGRATS!!!YOU WON!!!")
        user_wins += 1
#to play again
    play = input("WANNA PLAY AGAIN?????(yes/no)")  
    if play.lower() == "no":
        print("THANKYOU FOR PLAYING!!")
        print(f"Your score {user_wins}\nComputer score {computer_wins}")
        if user_wins > computer_wins:
            print("YOU ROCKED IT!!!! YOU WON")
        elif user_wins < computer_wins:
            print("HEY DON'T GIVE UP.....SEE YOU NEXT TIME")
        else:
            print("IT'S A TIE")
        break
