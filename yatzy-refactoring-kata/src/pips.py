from enum import Enum, unique

@unique
class Pips(Enum):
    
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    
    @classmethod
    def values(cls):
        return set(member.value for member in cls)
    
    @classmethod
    def names(cls):
        return [member.name for member in cls]
    
    @classmethod
    def items(cls):
        return [(member.name, member.value) for member in cls]

if __name__ == '__main__':
    print(Pips.values())
    print(Pips.names())
    print(Pips.items())
