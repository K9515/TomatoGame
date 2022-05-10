# rotten tomatoes game
My rotten tomatoes game randomly chooses a movie from a CSV file I created and prompts the user to input their guess of the movie's rotten tomatoes score. The use is then told what the correct score is, as well as if they got any points for their guess. This happens three times for player 1 and then the final point total is given.

Then, it is player 2's turn and they go through the exact same process as player 1. After their final point total is revealed the game tells the players who won or if they tied. 

My code is structured as follows:

          definitions for turns and points
          main while loop containing the game
          while loop for when player1_turns == 0 and player2_turns == 3
                              this is included here so player 1's total points can be printed before player 2 starts their turn
          while loop for randomly selecting a movie
                    This is where I struggled the most becuase I didn't want movies to repeat. This is overcome through a list that is added to every round. If a movie is randomly selected that is already in the list, my code will just keep randomly selecting until a movie is found that isn't in the list.
          2 while loops (one for player 1 and one for player 2) that ask for the player's guess
          difference taken between guess and the correct score
          if/elif/else statements that assign different point totals depending on the difference
          if statement for player 2 turns being up that breaks out of main while loop
          last while loop that determines who won or if they tied
          
For an example game this is what the output should look like:

          !!Welcome to the Rotten Tomatoes Guessing Game!!
          This is a 2 player game.Each player has three turns. You will be given the name of a movie and must input a guess. The player with the most points wins.
          It's Player 1's Turn:
          The movie is The Power of the Dog.
          Please input your guess: 
          98
          The correct answer was 93. Your guess was more than 10 off. You get 0 points.
          The movie is The Bad Guys.
          Please input your guess: 
          98
          The correct answer was 87. Your guess was more than 10 off. You get 0 points.
          The movie is Doctor Strange.
          Please input your guess: 
          98
          The correct answer was 89. Your guess was within 10 integers so you get 1 point.
          Player 1's total points: 1
          It's player 2's Turn:
          The movie is Along for the Ride.
          Please input your guess: 
          98
          The correct answer was 57. Your guess was more than 10 off. You get 0 points.
          The movie is Dune.
          Please input your guess: 
          98
          The correct answer was 83. Your guess was more than 10 off. You get 0 points.
          The movie is The Twin.
          Please input your guess: 
          98
          The correct answer was 50. Your guess was more than 10 off. You get 0 points.
          Player 2's total points: 0
          Player 1 wins with 1 point(s)! Player 2 had 0 point(s).
          
 Some things I would do if I had more time are figure out how to include a movie poster along with the movie title, allow users to choose number of rounds and players, and use on a much bigger data set.
 
 Included in the files here are my final code (final.py), my process(step1.py through step5.py), and my dataset (data.csv)
 My video goes much further in depth over these process files and the problems I encountered throughout creating this project.
