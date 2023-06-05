
class Human:

    def __init__(self, favNumber, favWord, tailLength):
        self.favNumber = favNumber
        self.favWord = favWord
        self.tailLength = tailLength

    
    def __add__(self, value):
        return self.favNumber + value
    
    def __str__(self) -> str:
        return self.favWord
    
    def __len__(self):
        return self.tailLength

human = Human(1,"two",0)

magicNumber = human + 7

print(human)

print(magicNumber)

print(len(human))