import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pips import Pips

class Yatzy:

    ZERO = 0
    FIFTEEN = 15
    TWENTY = 20
    FIFTY = 50
    
    @staticmethod
    def chance(*dice):
        '''
        1. The function can receive multiple parameters.
        2. Use sum() function to calculate the sum of the dice.  
        '''
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        3. Used a ternary operator to further simplify the function.
        '''
        return Yatzy.FIFTY if dice.count(dice[0]) == 5 else Yatzy.ZERO

    @staticmethod
    def ones(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        '''
        ONE = Pips.ONE.value
        return dice.count(ONE)

    @staticmethod
    def twos(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        '''
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        '''
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE
    
    @staticmethod
    def fours(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR
    
    @staticmethod
    def fives(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX
    
    @staticmethod
    def one_pair(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The variable result is used as an intermediate variable.
        4. First we filter the pairs, then with max() we get the highest pair.
        5. Renamed the function name to align it with the test.
        '''
        return max(list(filter(lambda x: dice.count(x) >= 2, dice)) , default=0) * 2

    @staticmethod
    def two_pair(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The variable result is used as an intermediate variable.
        4. First we filter the pairs, then with sum() we get the expected values.
        '''
        result = list(filter(lambda x: dice.count(x) >= 2, dice))
        return sum(list(set(result)) * 2) if len(result) >=4 else Yatzy.ZERO

    @staticmethod
    def three_of_a_kind(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The variable result is used as an intermediate variable.
        4. First we filter the pairs, then with sum() we get the expected values.
        '''
        result = list(filter(lambda x: dice.count(x) >= 3, dice))
        return sum(result[:3]) if len(result) >=3 else Yatzy.ZERO

    
    @staticmethod
    def four_of_a_kind(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The variable result is used as an intermediate variable.
        4. First we filter the pairs, then with sum() we get the expected values.
        '''
        result = list(filter(lambda x: dice.count(x) >= 4, dice))
        return sum(result[:4]) if len(result) >=4 else Yatzy.ZERO


    @staticmethod
    def small_straight(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        '''
        '''
        return 15 if len(set(sorted(dice))) == 5 and not set(sorted(dice)) > set([list(Pips.values())[5]]) else Yatzy.ZERO
        '''
        return Yatzy.FIFTEEN if set(dice) | {Pips.SIX.value} == Pips.values() else Yatzy.ZERO

    @staticmethod
    def large_straight(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        '''
        '''return 20 if len(set(sorted(dice))) == 5 and not set(sorted(dice)) > set([list(Pips.values())[0]]) else Yatzy.ZERO
        '''
        return Yatzy.TWENTY if set(dice) | {Pips.ONE.value} == Pips.values() else Yatzy.ZERO


    @classmethod
    def full_house(cls, *dice):
        '''
        dice_copy = set(dice)
        if len(dice_copy) == 2:
            result = 0
            for value in dice_copy:
                result += dice.count(value) * value
            return result
        return Yatzy.ZERO
        '''
        return cls.chance(*dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else Yatzy.ZERO