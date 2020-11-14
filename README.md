# Concept
This code is based off of the simple concept of designing a game that will pick a random number between a specified range (either by the user or default) and then the user will enter inputs one at a time and try to guess the value of the random number. Each guess will provide hints such as too low or too high so that the user can begin converging to the correct value. An additional feature has been added as well which will run the game using a binary search algorithm rather than having the user input guesses, and the algorithm will find the value within the range.

# Running
There are multiple ways to run this code based on the parameters passed into it. The program requires only 1 parameter passed into it, either a 0 or 1 which signifies which game mode to play the game in, where 0 represents manual playing where the user enters the guesses, and 1 signifies to run the code using a binary search algorithm to find the correct value. An example of how to compile the code is as follows:
```
python Random_Num.py 0
```
The above code will run the game in manual mode with the default range of guessing values to be 0-100. The user is able to pass two additional parameters into the function which will change the default value of the range:
```
python Random_Num.py 0 0 500
```
The above code will run the game in manual mode but now the range of values in which the number can lie is between 0 and 500. The same examples can be run except now the binary search algorithm will run the game for us:
```
python Random_Num.py 1 
python Random_Num.py 1 0 500
```
The above code will run the game just the same as the manual code except now we are using our binary search algorithm to play the game for us.

# Play again
After manually beating the game or once the binary search algorithm finishes the game, the user will be prompted with a question if they want to play again, and this can be answered with either Y for yes or N for no. If Y is typed the code will then rerun the same mode that was run the original time and depending on which mode was played a difference random range of values will be selected from a larger subset range. For example, if manual mode is played again, any random range will be selected from 0 : 1000 and for binary search mode the range increases to 0 : 30000 because of how quickly the algorithm performs.

### Author
Tyler Kawka