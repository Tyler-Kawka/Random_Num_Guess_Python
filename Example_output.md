Note: Extra line spacing in code is placed there for reading purposes, not actual output of code
# Example 1: Manual with default range
```
python Random_Num.py 0

Please enter your guess between 0 and 100: 50
Too high, try something lower
Please enter your guess between 0 and 100: 25
Too low, try something higher
Please enter your guess between 0 and 100: 35
Too high, try something lower
Please enter your guess between 0 and 100: 30
Too high, try something lower
Please enter your guess between 0 and 100: 27
Too low, try something higher
Please enter your guess between 0 and 100: 28
Congratulations you have guessed the number!
It only took you 6 tries!
Play again [Y,N]? : N
```

# Example 2: Manual with new range 
```
python Random_Num.py 0 -50 100

Please enter your guess between -50 and 100: 0
Too low, try something higher
Please enter your guess between -50 and 100: 50
Too low, try something higher
Please enter your guess between -50 and 100: 75
Too low, try something higher
Please enter your guess between -50 and 100: 85
Too high, try something lower
Please enter your guess between -50 and 100: 80
Too low, try something higher
Please enter your guess between -50 and 100: 82
Too low, try something higher
Please enter your guess between -50 and 100: 84
Too high, try something lower
Please enter your guess between -50 and 100: 83
Congratulations you have guessed the number!
It only took you 8 tries!

```

# Example 3: Binary Search Default Value
```
python Random_Num.py 1        

Running binary search algorithm on range 0 : 100
Guess 1 was: 50
Guess 2 was: 75
Guess 3 was: 62
Guess 4 was: 68
Guess 5 was: 65
Guess 6 was: 63
Guess 7 was: 64
Number is 64, Binary Search took 7 guesses!
Play again [Y,N]? : N
```

# Example 4: Binary Seach new range and play again
```
python Random_Num.py 1 0 50000

Running binary search algorithm on range 0 : 50000
Guess 1 was: 25000
Guess 2 was: 37500
Guess 3 was: 43750
Guess 4 was: 46875
Guess 5 was: 48438
Guess 6 was: 49219
Guess 7 was: 48828
Guess 8 was: 49023
Guess 9 was: 49121
Guess 10 was: 49170
Guess 11 was: 49194
Guess 12 was: 49206
Guess 13 was: 49200
Guess 14 was: 49197
Number is 49197, Binary Search took 14 guesses!
Play again [Y,N]? : Y

Game will be run on random value range between 0 : 30000
Running Binary Search algorithm on range 0 : 28887
Guess 1 was: 14443
Guess 2 was: 21665
Guess 3 was: 18054
Guess 4 was: 19859
Guess 5 was: 18956
Guess 6 was: 19407
Guess 7 was: 19181
Guess 8 was: 19068
Guess 9 was: 19124
Guess 10 was: 19096
Guess 11 was: 19110
Guess 12 was: 19117
Guess 13 was: 19113
Guess 14 was: 19115
Number is 19115, Binary Search took 14 guesses!
Play again [Y,N]? : N
```

### Author
Tyler Kawka