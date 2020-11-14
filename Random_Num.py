#Program that is based off random number guesser, incorporating a feature as well to allow user to toggle on binary search algorithm to find the number
from random import seed
import numpy as n
import sys

seed(1)
class Random_Num_Guess:
    #Constructor
    def __init__(self,mode,min=0,max=100):
        self.guesses = 0
        self.number = n.random.randint(min,max)
        self.min = min
        self.max = max
        self.mode = mode

    #Get guesses from user
    def get_guess(self):
        guess = input(f"Please enter your guess between " + str(self.min) + " and " + str(self.max) + ": " )
        if self.valid_guess(guess):
            return int(guess)
        else:
            print("That is not a valid guess, please try again")
            return self.get_guess()
    
    #Optional function that will run binary search and guess the number using algorithm
    def guess_num_binary_search(self,start,end):
        #double divide sign to floor the number
        middle = (start + end)//2
        #keep track of guesses
        self.guesses += 1
        
        #if middle value is smaller than the wanted value, cut out lower half and adjust to higher half
        if (middle < self.number):
            print("Guess " + str(self.guesses) + " was: " + str(middle))
            return self.guess_num_binary_search(middle+1,end)
        #if middle value is larger than the wanted value, cut out upper half and adjust to lower half
        elif (middle > self.number):
            print("Guess " + str(self.guesses) + " was: " + str(middle))
            return self.guess_num_binary_search(start,middle-1)
        #We found the number
        else:
            print("Guess " + str(self.guesses) + " was: " + str(middle))
            print("Number is " + str(self.number) + ", Binary Search took " +  str(self.guesses) + " guesses!")
            self.play_again()
        
    #Checking to see if guess out of range of min and max
    def valid_guess(self,num):
        return self.min <= int(num) <= self.max

    #Play again function to restart game
    def play_again (self):
        again = input("Play again [Y,N]? : ")
        if again == "Y":
            if self.mode == 0:
                print("Game will be run on random value range between 0 : 1000")
                next_game = Random_Num_Guess(0,0,n.random.randint(1,1000))
                next_game.play()
            else:
                print("Game will be run on random value range between 0 : 30000")
                next_game = Random_Num_Guess(1,0,n.random.randint(1,30000))
                print("Running Binary Search for number with range of " + str(next_game.min) + " : "  + str(next_game.max))
                next_game.guess_num_binary_search(next_game.min,next_game.max)
        else:
            exit()
            
    #Manual play loop
    def play(self):
        while 1:
            self.guesses += 1
            guess = self.get_guess()
            if guess < self.number:
                print("Too low, try something higher")
            elif guess > self.number:
                print("Too high, try something lower")
            else:
                break
        print("Congratulations you have guessed the number!")
        print("It only took you " + str(self.guesses) + " tries!")
        self.play_again()
    
if (len(sys.argv) == 1):
    print("Usage: Enter parameter 0 for manual play, 1 for Binary Search algorithm")
    exit()
elif (len(sys.argv) == 2):
    if (int(sys.argv[1])== 0):
        newgame = Random_Num_Guess(0)
        newgame.play()
    elif (int(sys.argv[1])==1):
        newgame = Random_Num_Guess(1)
        print("Running binary search algorithm on range " + str(newgame.min) + " : " + str(newgame.max))
        newgame.guess_num_binary_search(newgame.min,newgame.max)
    else:
        print("Not a valid argument, exiting " + sys.argv[1])
        exit()
elif (len(sys.argv) == 4):
    if (int(sys.argv[1])==0):
        newgame = Random_Num_Guess(0,int(sys.argv[2]),int(sys.argv[3]))
        newgame.play()
    elif (int(sys.argv[1])==1):
        newgame = Random_Num_Guess(1,int(sys.argv[2]),int(sys.argv[3]))
        print("Running binary search algorithm on range " + str(newgame.min) + " : " + str(newgame.max))
        newgame.guess_num_binary_search(newgame.min,newgame.max)
    else:
        print("Not a valid argument, exiting")
        exit()


