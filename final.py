#Tomato Game
import pandas
from itertools import chain
import numpy as np
usedlist = [] 
#empty list
def main():
    print('!!Welcome to the Rotten Tomatoes Guessing Game!!\r\n\nThis is a 2 player game.Each player has three turns. You will be given the name of a movie and must input a guess. The player with the most points wins.\n')
    player1_turns = 3
    player2_turns = 3
    points = 0
    player2_points= 0
    #what points will be added to and where turns are kept track of
    print("It's Player 1's Turn:\n")
    while True:
        while player1_turns == 0 and player2_turns == 3:
            #after player 1's turns and before player 2 starts
            print(f"Player 1's total points: {points}\n")
            print("It's Player 2's Turn:\n")
            break
        while True:
            #get movie id
            data = pandas.read_csv("data.csv")
            choice = np.random.choice(data.name, replace=False)
            if choice not in usedlist:
                #means haven't guessed this movie before
                secret = (data[data.name == choice])
                moviename = secret.name.values 
                scorevalue = secret.score.values
                scorevalue2 = str(scorevalue)[1:-1]
                usedlist.append(choice)
                print(f"The movie is {','.join(moviename)}.")
                break
        while player2_turns > 0 and player1_turns == 0:
            #player 2 guess
            try:
                guess = int(input('Please input your guess: \n'))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...\n')
        while player1_turns > 0:
            #player 1 guess
            try:
                guess = int(input('Please input your guess: \n'))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...\n')
        difference = guess - scorevalue
        #how accurate is the guess
        if difference in chain(range(-5,0), range(1,6)):
            print(f"\nThe correct answer was {scorevalue2}. Your guess was within 5 integers so you get 5 points.\n")
            if player1_turns > 0:   
                points = points+5
                player1_turns -= 1
            else:
                player2_points = player2_points+5  
                player2_turns -= 1
        elif difference in chain(range(-10,-5), range(6, 11)):
            print(f"\nThe correct answer was {scorevalue2}. Your guess was within 10 integers so you get 1 point.\n")
            if player1_turns > 0:   
                points = points+1
                player1_turns -= 1
            else:
                player2_points = player2_points+1
                player2_turns -= 1
        elif difference == 0:
            print('\nYou guessed correctly! You get 10 points.\n')
            if player1_turns > 0:  
                points = points+10
                player1_turns -= 1
            else:
                player2_points = player2_points+10
                player2_turns -= 1
        else:
            print(f"\nThe correct answer was {scorevalue2}. Your guess was more than 10 off. You get 0 points.\n")
            if player1_turns > 0:  
                player1_turns -= 1
            else:
                player2_turns -= 1
        if player2_turns == 0:
            #game over
            break
    while player2_turns == 0:
        #determines who won and final point totals
        print(f"Player 2's total points: {player2_points}\n")
        if points > player2_points:
            print(f"Player 1 wins with {points} point(s)! Player 2 had {player2_points} point(s).\n")
            break
        elif player2_points > points:
            print(f"Player 2 wins with {player2_points} point(s)! Player 1 had {points} point(s).\n")
            break
        elif player2_points == points:
            print(f"You Tied with {player2_points} point(s).\n")
            break

if __name__ == '__main__':
    main()