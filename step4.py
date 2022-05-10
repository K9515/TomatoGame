#Tomato Game

import random
import pandas
from itertools import chain
import numpy as np
usedlist = []
def random_movie():
    data = pandas.read_csv("data.csv")
    choice = np.random.choice(data.score, replace=False)
    while True:
        if choice in usedlist:
            break
        else:
            secret = (data[data.score == choice])
            moviename = secret.name.values 
            scorevalue = secret.score.values
            scorevalue2 = str(scorevalue)[1:-1]
            usedlist.append(choice)
            return moviename, scorevalue2, choice, data
    #print(data[data['score'] == scorevalue2].index.values)
    #id = secret.id
    #print(scorevalue2)
    #data.set_index('id', inplace=True)
    #data.drop(data[data['score'] == scorevalue2].index.values, axis=0, inplace=True)
    #return moviename, scorevalue2, choice, data
#def random_movie2():
    #choice = np.random.choice(data.score, replace=False)
    #secret = (data[data.score == choice])
    #moviename = secret.name.values 
    #scorevalue = secret.score.values
    #scorevalue2 = str(scorevalue)[1:-1]
    #print(data[data['score'] == scorevalue2].index.values)
    #id = secret.id
    #print(scorevalue2)
    #data.set_index('id', inplace=True)
    #data.drop(data[data['score'] == scorevalue2].index.values, axis=0, inplace=True)
    #return moviename, scorevalue2, choice, data

    
def main():
    print('Welcome to Guess the Rotten Tomatoes Score.') 
    print('This is a 2 player game.I will give you the name of a movie and you input a guess. Each player has three turns. The player with the most points wins.')
    
    player1_turns = 3
    player2_turns = 3
    points = 0
    player2_points= 0
    print("It's Player 1's Turn:")
    while True:
        #pull movie id 
        while player1_turns == 0 and player2_turns == 3:
            print(f"Player 1's total points: {points}")
            print("It's player 2's Turn:")
            break
        #if player1_turns == 3:
        randommovie = random_movie()
        moviename = randommovie[0]
        scorevalue2 = randommovie[1]
        choice = randommovie[2]
        #else:
            #choice = np.random.choice(data.score, replace=False)
            #secret = (data[data.score == choice])
            #moviename = secret.name.values 
            #scorevalue = secret.score.values
            #scorevalue2 = str(scorevalue)[1:-1]
            #data.drop(data[data['score'] == scorevalue2].index.values, axis=0, inplace=True)
        print(f"The movie is {','.join(moviename)}.")
        #print(data)
        while player2_turns > 0 and player1_turns == 0:
            try:
                guess = int(input('Please input your guess: '))
                player2_turns -= 1
                print("yes)")
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        # Grab a guess from the player
        while player1_turns > 0:
            try:
                guess = int(input('Please input your guess: '))
                player1_turns -= 1
                print("no")
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        difference = guess - choice
        if difference in [x for x in range(-5,5) if x != 0]:
            print(f"The correct answer was {scorevalue2}. Your guess was within 5 integers so you get 5 points.")
            if player1_turns > 0:   
                points = points+5
            else:
                player2_points = player2_points+5    
        elif difference in chain(range(-10, -6), range(6, 10)):
            print(f"The correct answer was {scorevalue2}. Your guess was within 10 integers so you get 1 point.")
            if player1_turns > 0:   
                points = points+1
            else:
                player2_points = player2_points+1   
        elif difference == 0:
            print('You guessed correctly! You get 10 points.')
            if player1_turns > 0:  
                points = points+10
            else:
                player2_points = player2_points+10
        else:
            print(f"The correct answer was {scorevalue2}. Your guess was within more than 10 off. You get 0 points.")

        while player2_turns == 0:
            print(f"Player 2's total points: {player2_points}")
            if points > player2_points:
                print(f"Player 1 wins with {points} points! Player 2 had {player2_points} points.")
                break
            elif player2_points > points:
                print(f"Player 2 wins with {player2_points} points! Player 1 had {points} points.")
                break
            elif player2_points == points:
                print(f"You Tied with {player2_points} points.")
                break
        if player2_turns == 0:
            break
if __name__ == '__main__':
    main()