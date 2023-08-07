import abc


class DevourFood(abc.ABC):
    """
    Abstract class for animals that eat food
    """
    def __init__(self) -> None:
        pass

    @abc.abstractclassmethod
    def eatFood():
        """
        Abstract fun to be implemented by the child classes
        """
        pass 
"""
Implementation
"""
class Duck(DevourFood):
    def __init__(self) -> None:
        super().__init__()

    def eatFood(self):
        print('eating duck food')

class Dog(DevourFood):
    def __init__(self) -> None:
        super().__init__()

    def eatFood(self):
        print('eating dog food')


x =Duck()
x.eatFood()