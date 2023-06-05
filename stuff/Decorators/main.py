from decorators import to_Uppercase
from decorators import to_List


@to_List
def yo(word):
    return word

print(yo("word"))
