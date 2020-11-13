from random import seed
import numpy as n
import sys

seed(1)
class Random_Num_Guess:
    def __init__(self,min=0,max=100):
        self.guesses = 0
        self.number = n.random.randint(min,max)
        self.min = min
        self.max = max
    
    def get_guess(self):
        guess = input(f"Please enter your guess between " + str(self.min) + " and " + str(self.max) + ": " )
        if self.valid_guess(guess):
            return int(guess)
        else:
            print("That is not a valid guess, please try again")
            return self.get_guess()

    def valid_guess(self,num):
        return self.min <= int(num) <= self.max
    
    def play_again (self):
        again = input("Play again [Y,N]? Game will be run with random value range between 0-1000: ")
        if again == "Y":
            next_game = Random_Num_Guess(0,n.random.randint(1,1000))
            next_game.play()
        else:
            exit()

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
     
if (len(sys.argv) < 2):
    newgame = Random_Num_Guess()
    newgame.play()
else:
    newgame = Random_Num_Guess(int(sys.argv[1]),int(sys.argv[2]))
    newgame.play()