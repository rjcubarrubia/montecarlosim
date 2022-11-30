import numpy as np
import pandas as pd


class Die():
    '''
    Creates die object. 
    Contains the methods:
        __init__
        change_weight
        roll
        show
    '''
    
    
    def __init__(self, faces):
        '''
        Accepts an array of faces as an argument. Faces must be unique. 
        Initializes the weights for the faces as 1.0 as default. 
        Weights can be changed later with .change_weight method. 
        Creates a private data frame of faces and weights.
        '''
        
        flag = len(set(faces)) == len(faces)
        if flag == 0:
            #print("Each face must be unique.")
            raise ValueError("Each face must be unique.")
        
        weights = np.ones(len(faces))
                      
        self._faces_and_weights_df = pd.DataFrame({'Faces': faces, 'Weights': weights})
        
        
    def change_weight(self, face, weight):
        '''
        Accepts a face and a weight argument. Face argument is the face value to be changed and weight argument is the new weight.
        Checks to see if the face passed is indeed in the array of weights.
        Converts weight to float. 
        Changes the weight of the die that corresponds with the face that is passed.
        '''
        
        weight = float(weight)
        
        if face not in list(self._faces_and_weights_df['Faces']):
            #print("Face is not in the initialized die.")
            raise ValueError("Face is not in the created die.")
            
        face_row_index = list(self._faces_and_weights_df.index[self._faces_and_weights_df['Faces'] == face])[0]
        self._faces_and_weights_df.loc[face_row_index, 'Weights'] = weight
        
        
    def roll(self, rolls = 1):
        '''
        Rolls the die. Accepts rolls as an argument. Rolls defaults to 1. 
        '''
        
        rolled_faces_and_weights_df = (self._faces_and_weights_df.sample(n = rolls, replace = True, weights = 'Weights').
                                       reset_index(drop = True))
        
        return list(rolled_faces_and_weights_df['Faces'])
        
    def show(self):
        '''
        Returns the faces and weights of the initialized die.
        '''
        
        return self._faces_and_weights_df
        

class Game():
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
    
    def __init__(self, dice_list):
        '''
        Initializes game object. 
        Accepts a list of similar die objects as an argument. Dice have already been instantiated with Die class.
        '''
        
        self.dice_list = dice_list
        
        
    def play(self, rolls):
        '''
        Accepts number of rolls as an argument. 
        Creates private data frame of rolls as observations (rows) and dice as features (columns).
        Elements of dataframe are [roll, die face result of roll].
        '''
        
        self._rolls_and_dice_df = pd.DataFrame()
        self._rolls_and_dice_df.index.rename("Roll Number", inplace = True)
        
        for die in range(0, len(self.dice_list)):
            self._rolls_and_dice_df[die] = self.dice_list[die].roll(rolls)
            
    
    def show(self, wide_or_narrow = 'wide'):
        '''
        Accepts "wide" or "narrow" as arguments for the type of data frame desired. 
        Argument defaults to "wide" data frame.
        Returns the data frame of rolls and faces. 
        '''
        
        if wide_or_narrow == 'wide':
            return self._rolls_and_dice_df
        
        elif wide_or_narrow == 'narrow':
            rolls_and_dice_df_narrow = self._rolls_and_dice_df.stack().to_frame('Faces')
            rolls_and_dice_df_narrow.index.rename(["Roll Number", "Dice"], inplace = True)
            return rolls_and_dice_df_narrow
        
        else:
            #print("Argument must be either "narrow" or "wide" for the type of data frame desired.")
            raise ValueError("Argument must be either \"narrow\" or \"wide\" for the type of data frame desired.")
            

class Analyzer():
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
        
    
    def __init__(self, game):
        '''
        Initializes analyzer object.
        Accepts a game object as an argument.
        '''
        
        self._game = game
            
        
    def face_counts_per_roll(self):
        '''
        Creates data frame containing the amount of times a face appears in each roll.
        This data frame is the public attribute face_counts_per_roll_df
        Rows are rolls; columns are faces in the dice.
        '''
        
        game_df_narrow = self._game.show("narrow")
        self.face_counts_per_roll_df = (game_df_narrow.groupby("Roll Number").value_counts().
                                        to_frame()[0].unstack().fillna(0).astype(int))
        
        
    def jackpot(self):
        '''
        Counts the amount of rolls that resulted in all faces being the same.
        Creates data frame that tracks each jackpot. with rolls as rows and faces as columns.
        This data frame is the public attribute jackpot_df
        Returns the count of jackpots rolled.
        Count of jackpots is also the public attribute jackpot_count
        '''
        
        game_df = self._game.show()
        self.jackpot_df = game_df[game_df.nunique(1) == 1]
        
        self.jackpot_count = int(len(self.jackpot_df))
        
        return self.jackpot_count
        print("There was/were " + str(self.jackpot_count) + " jackpot(s).")
    
    
    def combo(self):
        '''
        Creates data frame with multi-columned index. 
        Rows are combinations and column is how many times that combination appeared.
        This data frame is the public attribute combo_df
        Creates a count of how many unique combinations were rolled. 
        This count is the public attribute combo_count
        '''
        
        game_df = self._game.show()
        
        self.combo_df = game_df.apply(lambda x: x.sort_values().squeeze(), axis=1).value_counts().to_frame('count')
        self.combo_count = len(self.combo_df)    
        
        
    def permutations(self):
        '''
        Counts the amount of permuations that appeared.
        This count is the public attribute permutation_count
        '''
        
        self.permutation_count = self._game.show().value_counts(ascending = False).reset_index(name = 'count')
        
