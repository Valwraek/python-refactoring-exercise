from src.yatzy1 import Yatzy


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():
    '''
    Refactored due to redundant variables
    '''
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy_scores_50():
    '''
    1. Refactored due to redundant variables.
    '''
    assert 50 == Yatzy.yatzy(4, 4, 4, 4, 4)
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)


def test_ones():
    '''
    1. Changed the name of the test to align it with the function that is tested.
    2. Moved the order of the first assert to have the same structure as the other tests.
    '''
    assert 1 == Yatzy.ones(1, 2, 3, 4, 5) 
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)


def test_twos():
    '''
    1. Changed the name of the test to align it with the function that is tested.
    2. Added a test case to test the function with the number 2.
    '''
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)
    assert 0 == Yatzy.twos(6, 1, 3, 4, 5)
    


def test_threes():
    '''
    1. Changed the name of the test to align it with the function that is tested.
    2. Added a test case to test the function with the number 3.
    '''
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)
    assert 0 == Yatzy.threes(1, 2, 2, 1, 5)


def test_fours():
    '''
    1. Changed the name of the test due to redundancy in it's naming.
    2. The test no longer creates objects and behaves like the others.
    '''
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)
    assert 0 == Yatzy.fours(1, 2, 2, 1, 5)
    


def test_fives():
    '''
    1. The test no longer creates objects and behaves like the others.
    '''
    assert 10 == Yatzy.fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)
    assert 0 == Yatzy.fives(1, 2, 2, 1,6)
    

def test_sixes():
    '''
    1. Changed the name of the test due to redundancy in it's naming.
    2. The test no longer creates objects and behaves like the others.
    '''
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)
    assert 0 == Yatzy.fives(1, 2, 2, 1,4)
    


def test_one_pair():
    '''
    1. The test no longer creates objects.
    '''
    assert 6 == Yatzy.one_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy.one_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.one_pair(5, 3, 6, 6, 5)
    assert 0 == Yatzy.one_pair(1, 2, 3, 4, 5)

def test_two_pair():
    '''
    1. The test no longer creates objects.
    '''
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)
    assert 0 == Yatzy.two_pair(2, 1, 6, 5, 4)


def test_three_of_a_kind():
    '''
    1. Test no longer creates objects. 
    '''
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)


def test_four_of_a_kind():
    '''
    1.Renamed the name of the test.
    '''
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_small_straight():
    '''
    1. Renamed the name of the test.
    2. Renamed the tests.
    '''
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.small_straight(1, 2, 2, 4, 5)


def test_large_straight():
    '''
    1. Renamed the name of the test.
    2. Renamed the tests.
    '''
    assert 20 == Yatzy.large_straight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 2, 4, 5)
    assert 0 == Yatzy.large_straight(2, 2, 6, 4, 5)


def test_full_house():
    '''
    1. Renamed the name of the test.
    2. Renamed the tests.
    '''
    assert 18 == Yatzy.full_house(6, 2, 2, 2, 6)
    assert 0 == Yatzy.full_house(2, 3, 4, 5, 6)
    assert 0 == Yatzy.full_house(2, 2, 2, 2, 6)
    