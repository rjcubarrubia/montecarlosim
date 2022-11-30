# montecarlosim  
A Monte Carlo simulator package created for DS5100 course in UVA MSDS program  


## Metadata  
Name: RJ Cubarrubia    
Project Name: montecarlosim  


## Demo Code  
Install from root of montecarlosim with pip install .  
Import with from montecarlosim import *  

### An example of creating a 6 sided die object, one fair and one unfair with the 6 face reweighted from 1 to 5, and rolling the fair die twice:  
six_sided = \[1, 2, 3, 4, 5, 6\]  

fair_die1 = Die(six_sided)  

unfair_die1 = Die(six_sided)  
unfair_die1.change_weight(6, 5)  

fair_die1.roll(2)  

### Playing a game with 1000 rolls of 3 dice and checking the data frame in wide (default) and narrow formats:  
fair_die_list = \[fair_die1, fair_die2, fair_die3\]  
fair_die_game = Game(fair_die_list)  

fair_die_game.play(1000)  

fair_die_game.show()  
fair_die_game.show("narrow")  

### Analyzing the game that was just played by checking the data frame of all rolls and checking for jackpots, combos and permutations:  
fair_die_game_analyzer = Analyzer(fair_die_game)  

fair_die_game_analyzer.face_counts_per_roll()  
fair_die_game_analyzer.face_counts_per_roll_df  

fair_die_game_analyzer.jackpot()  
(jackpot method will return the counts)  
fair_die_game_analyzer.jackpot_df  

fair_die_game_analyzer.combo()  
fair_die_game_analyzer.combo_df  
fair_die_game_analyzer.combo_count  

fair_die_game_analyzer.permutations()  
fair_die_game_analyzer.permutation_count  


## API Description  
### Classes  
#### Die()  
'''
Creates die object.  
Contains no public attributes.  
Contains the methods:  
__init__  
change_weight  
roll  
show  
'''  

__init__(self, faces):  
'''  
Accepts an array of faces as an argument. Faces must be unique.  
Initializes the weights for the faces as 1.0 as default.  
Weights can be changed later with .change_weight method.  
Creates a private data frame of faces and weights.  
'''  

change_weight(self, face, weight):  
'''  
Accepts a face and a weight argument. Face argument is the face value to be changed and weight argument is the new weight.  
Checks to see if the face passed is indeed in the array of weights.  
Converts weight to float.  
Changes the weight of the die that corresponds with the face that is passed.  
'''  

roll(self, rolls = 1):  
'''  
Rolls the die. Accepts rolls as an argument. Rolls defaults to 1.  
'''  

show(self):  
'''  
Returns the faces and weights of the initialized die.  
'''  

#### Game()  
'''  
Creates a game of rolling one or more die of the same kind one or more times.  
Dice have the same number of sides and set of faces but each die can have its own weights.  
Contains no public attributes.  
show() method returns data frame can be made narrow or wide.  
Contains the methods:  
__init__  
play  
show  
'''  

__init__(self, dice_list):  
'''  
Initializes game object.  
Accepts a list of similar die objects as an argument. Dice have already been instantiated with Die class.  
'''  

play(self, rolls):  
'''  
Accepts number of rolls as an argument.  
Plays a game that rolls the all the dice the number of times specified in rolls argument.  
'''  

show(self, wide_or_narrow = "wide"):  
'''  
Accepts "wide" or "narrow" as arguments for the type of data frame desired.   
Argument defaults to "wide" data frame.  
Returns the data frame of rolls and faces.  
'''  

#### Analyzer()  
'''  
Analyzes the dice game after the game is played.  
Contains the following public attributes:  
face_counts_per_roll_df  
jackpot_df  
jackpot_count  
permutation_count  
combo_df  
combo_count  
Contains the following methods:  
__init__  
face_counts_per_roll  
jackpot  
permutations  
combo  
'''  

__init__(self, game):  
'''  
Initializes analyzer object.  
Accepts a game object as an argument.  
'''  

face_counts_per_roll(self):  
'''  
Creates data frame containing the amount of times a face appears in each roll.  
This data frame is the public attribute face_counts_per_roll_df  
Rows are rolls; columns are faces in the dice.  
'''  

jackpot(self):  
'''  
Counts the amount of rolls that resulted in all faces being the same.  
Creates data frame that tracks each jackpot. with rolls as rows and faces as columns.  
This data frame is the public attribute jackpot_df  
Returns the count of jackpots rolled.  
Count of jackpots is also the public attribute jackpot_count  
'''

combo(self):  
'''  
Creates data frame with multi-columned index.  
Rows are combinations and column is how many times that combination appeared.  
This data frame is the public attribute combo_df  
Creates a count of how many unique combinations were rolled.  
This count is the public attribute combo_count  
'''  

permutations(self):  
'''  
Counts the amount of permuations that appeared.  
This count is the public attribute permutation_count  
'''  
