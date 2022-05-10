#Tomato Game

import random
import pandas
from itertools import chain
import numpy as np
def random_movie():
    data = pandas.read_csv("data.csv")
    choice = np.random.choice(data.score, replace=False)
    secret = (data[data.score == choice])
    moviename = secret.name.values 
    scorevalue = secret.score.values
    scorevalue2 = str(scorevalue)[1:-1]
    #print(scorevalue2)
    datadrop = data.drop(data[data['score'] == scorevalue2].index,inplace=True)
    return moviename, scorevalue2, choice, datadrop
    
def main():
    print('Welcome to Guess the Rotten Tomatoes Score.') 
    print('This is a 2 player game.I will give you the name of a movie and you input a guess. Each player has three turns. The player with the most points wins.')
    
    player1_turns = 3
    player2_turns = 3
    points = 0
    player2_points= 0
    print("It's Player 1's Turn:")
    while player1_turns > 0:
        #pull movie id 

        randommovie = random_movie()
        moviename = randommovie[0]
        scorevalue2 = randommovie[1]
        choice = randommovie[2]
        print(f"The movie is {','.join(moviename)}.")
        # Grab a guess from the player
        while True:
            try:
                guess = int(input('Please input your guess: '))
                player1_turns -= 1
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        # print(f'You guessed {guess}')
        difference = guess - choice
        if difference in [x for x in range(-5,5) if x != 0]:
            print(f"The correct answer was {scorevalue2}. Your guess was within 5 integers so you get 5 points.")
            points = points+5
            
        elif difference in chain(range(-10, -6), range(6, 10)):
            print(f"The correct answer was {scorevalue2}. Your guess was within 10 integers so you get 1 point.")
            points = points+1
        elif difference == 0:
            print('You guessed correctly! You get 10 points.')
            points = points+10
        else:
            print(f"The correct answer was {scorevalue2}. Your guess was within more than 10 off. You get 0 points.")
    print(f"Player 1's total points: {points}")
    print("It's player 2's Turn:")
    while player2_turns > 0:
        #pull movie id 
        randommovie = random_movie()
        moviename = randommovie[0]
        scorevalue2 = randommovie[1]
        choice = randommovie[2]
        print(f"The movie is {','.join(moviename)}.")
        # Grab a guess from the player
        while True:
            try:
                guess = int(input('Please input your guess: '))
                player2_turns -= 1
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        # print(f'You guessed {guess}')
        difference = guess - choice
        if difference in [x for x in range(-5,5) if x != 0]:
            print(f"The correct answer was {scorevalue2}. Your guess was within 5 integers so you get 5 points.")
            player2_points = player2_points+5
            
        elif difference in chain(range(-10, -6), range(6, 10)):
            print(f"The correct answer was {scorevalue2}. Your guess was within 10 integers so you get 1 point.")
            player2_points = player2_points+1
        elif difference == 0:
            print('You guessed correctly! You get 10 points.')
            player2_points = player2_points+10
        else:
            print(f"The correct answer was {scorevalue2}. Your guess was within more than 10 off. You get 0 points.")
    print(f"Player 2's total points: {player2_points}") 
    if points > player2_points:
        print(f"Player 1 wins with {points} points! Player 2 had {player2_points} points.")
    elif player2_points > points:
        print(f"Player 2 wins with {player2_points} points! Player 1 had {points} points.")
    elif player2_points == points:
        print(f"You Tied with {player2_points} points.")
if __name__ == '__main__':
    main()