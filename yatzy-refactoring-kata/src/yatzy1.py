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
        return dice.count(1)

    @staticmethod
    def twos(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        '''
        return dice.count(2) * 2

    @staticmethod
    def threes(*dice):
        '''
        1. The function can receive multiple parameters.
        2. The method ".count()" to simplify an overly complex function.
        '''
        return dice.count(3) * 3
    
    @staticmethod
    def fours(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        return dice.count(4) * 4
    
    @staticmethod
    def fives(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        return dice.count(5) * 5
    
    @staticmethod
    def sixes(*dice):
        '''
        1. Removed the use of objects.
        2. The function can receive multiple parameters.
        3. The method ".count()" to simplify an overly complex function.
        '''
        return dice.count(6) * 6
    
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
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

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