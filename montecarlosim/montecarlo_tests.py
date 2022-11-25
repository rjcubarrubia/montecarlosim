import numpy as np
import pandas as pd
from montecarlosim import *
import unittest

class MonteCarloSimTestSuite(unittest.TestCase):
    '''
    Unit Test suite for MonteCarloSim package.
    Tests Die class, Game class and Analyzer class.
    '''
    
    def test_1_change_weight(self):
        '''
        Tests change_weight method in Die class.
        '''
        faces1 = [1, 2]
        die1 = Die(faces1)
        
        die1.change_weight(2, 3)
        
        die1_df = die1._faces_and_weights_df
        testdie1_df = pd.DataFrame({'Faces': [1, 2], 'Weights': [1, 3]})
        
        die1_df_testcell = die1_df.loc[1, "Weights"]
        testdie1_df_testcell = testdie1_df.loc[1, "Weights"]
        
        self.assertEqual(die1_df_testcell, testdie1_df_testcell)
        
                                       
    def test_2_roll(self):
        '''
        Tests roll method in Die class.
        '''
        die2 = Die([1, 2])
        
        test2_length = 5
                                       
        self.assertEqual(len(die2.roll(5)), test2_length)
    
                                       
    def test_3_show(self):
        '''
        Tests show method in Die class.
        '''
        die3 = Die([1, 2])
        
        die3_shape = die3.show().shape
        test_shape = (2, 2)
        
        self.assertEqual(die3_shape, test_shape)
                                       
                                       
    def test_4_play(self):
        '''
        Tests play method in Game class.
        '''                              
        sixsided = [1, 2, 3, 4, 5, 6]

        testdie1 = Die(sixsided)
        testdie2 = Die(sixsided)
        testdie3 = Die(sixsided)
        testdie4 = Die(sixsided)

        testdielist = [testdie1, testdie2, testdie3, testdie4]

        testgame = Game(testdielist)
        testgame.play(5)
        testgame_df = testgame._rolls_and_dice_df

        testgame_df_shape = testgame_df.shape
        test_shape = (5, 4)
                                       
        self.assertEqual(testgame_df_shape, test_shape)
                                    
                                       
    def test_5_show(self):
        '''
        Tests show method in Game class.
        '''
        sixsided = [1, 2, 3, 4, 5, 6]

        testdie1 = Die(sixsided)
        testdie2 = Die(sixsided)
        testdie3 = Die(sixsided)
        testdie4 = Die(sixsided)

        testdielist = [testdie1, testdie2, testdie3, testdie4]

        testgame2 = Game(testdielist)
        testgame2.play(5) 
        testgame2_df = testgame2.show()
                                       
        testgame2_df_shape = testgame2_df.shape
        test_shape2 = (5, 4)
                                       
        self.assertEqual(testgame2_df_shape, test_shape2)
                                       
    
    def test_6_face_counts_per_roll(self):
        '''
        Tests face_counts_per_roll method in Analyzer class.
        '''
        twosided = [1, 2]

        testcoin1 = Die(twosided)
        testcoinlist = [testcoin1]
        testgame3 = Game(testcoinlist)
        testgame3.play(1)

        testgame3analyzer = Analyzer(testgame3)
        testgame3analyzer.face_counts_per_roll()
                                       
        analyzer_value = testgame3analyzer.face_counts_per_roll_df.iloc[0, 0]
        test_value = 1
                                       
        self.assertEqual(analyzer_value, test_value)
                                       
                                       
    def test_7_jackpot(self):
        '''
        Tests jackpot method in Analyzer class.
        '''
        twosided = [1, 2]
                                       
        testcoin1 = Die(twosided)
        testcoin2 = Die(twosided)
        testcoin3 = Die(twosided)
                                       
        testcoin1.change_weight(2, 0)
        testcoin2.change_weight(2, 0)
        testcoin3.change_weight(2, 0)
                                       
        testcoinlist = [testcoin1, testcoin2, testcoin3]
        testgame4 = Game(testcoinlist)
        testgame4.play(5)
                                       
        testgame4analyzer = Analyzer(testgame4)
                                       
        test4jackpots = testgame4analyzer.jackpot()
        testvalue = 5
                                       
        self.assertEqual(test4jackpots, testvalue)
                                       
                                       
   #def test_8_combo(self):
        #'''
        #Tests combo method in Analyzer class.
        #'''
                                       
                                       
    def test_9_permutations(self):
        '''
        Tests permutations method in Analyzer class.
        '''
        twosided = [1, 2]
                                       
        testcoin1 = Die(twosided)
        testcoin2 = Die(twosided)
        testcoin3 = Die(twosided)
                                       
        testcoin1.change_weight(2, 0)
        testcoin2.change_weight(2, 0)
        testcoin3.change_weight(2, 0)
                                       
        testcoinlist = [testcoin1, testcoin2, testcoin3]
        testgame5 = Game(testcoinlist)
        testgame5.play(5)
                                       
        testgame5analyzer = Analyzer(testgame5)
        testgame5analyzer.permutations()
                                       
        testgame5permutations = len(testgame5analyzer.permutation_count)
        testvalue = 1
                                       
        self.assertEqual(testgame5permutations, testvalue)
                                       
                                       
if __name__ == '__main__':

    unittest.main(verbosity = 3)
                                       
