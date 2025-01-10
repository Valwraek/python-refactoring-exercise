from src.pips import Pips

class Yatzy:

    ZERO = 0
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
        result = max(list(filter(lambda x: dice.count(x) >= 2, dice)) , default=0) * 2
        return result

    @staticmethod
    def two_pair(*dice):
        
        result = list(filter(lambda x: dice.count(x) >= 2, dice))
        return sum(list(set(result)) * 2) if len(result) >=4 else Yatzy.ZERO

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0