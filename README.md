# rotten tomatoes game
After a meeting, I've decided to instead make a game based off of rotten tomatoes and my love for movies. It is a guessing game akin to the guess the number game in class, but with points assigned according to how close to the answer one guesses. 

The goal by the end of this is to create a working prototype for a small dataset (like the small dataset from PSET 4 in class). 
Here are my steps:
1) first create a file of Movies and their corresponding rotten tomato scores. 10 or so movies should do so I can test my code throughout the process of creating.
2) import the guessing the number code and edit to broadly represent what I want to do
          here is the primary loop I am thinking of
                  randomly select one movie
                  ask user for a guess
                  if the guess is within 10 -- 1 point
                                          5 -- 5 points
                                    correct -- 10 points
                  add points to score
                  tell user points gained
         do this loop twice more
         give user final point total
         
         do the exact same thing for player two
         
         determine which point total is bigger
         tell user who won or if they tied
         
current code
      define above the actual game
            player1_turns = 3
            player2_turns = 3
            points = 0
            player2_points= 0
      what i currently have for the game
      while True:
            try:
                guess = int(input('Please input your guess: '))
                player1_turns -= 1
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        difference = guess - (random movie score)
        if difference in [x for x in range(-5,5) if x != 0]:
            print(f"The correct answer was (random movie score). Your guess was within 5 integers so you get 5 points.")
            points = points+5
        elif difference in chain(range(-10, -6), range(6, 10)):
            print(f"The correct answer was (random movie score). Your guess was within 10 integers so you get 1 point.")
            points = points+1
        elif difference == 0:
            print('You guessed correctly! You get 10 points.')
            points = points+10
        else:
            print(f"The correct answer was (random movie score). Your guess was within more than 10 off. You get 0 points.") 
