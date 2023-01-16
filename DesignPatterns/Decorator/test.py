class WrittenText:

    """Represents a Written text"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper(WrittenText):

    """Wraps a tag in <u>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())


class ItalicWrapper(WrittenText):

    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


class BoldWrapper(WrittenText):

    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


""" main method """

if __name__ == "__main__":

    before_gfg = WrittenText("GeeksforGeeks")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print("before :", before_gfg.render())
    print("after :", after_gfg.render())



import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.1*self.get_cost()

class Concrete_Coffee(Abstract_Coffee):
   
   def get_cost(self):
      return 1.00
   
   def get_ingredients(self):
      return 'coffee'

@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):
   
   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.25
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.75
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', vanilla'
# The implementation of the abstract class of the coffee shop is done with a separate file as mentioned below −

import coffeeshop

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))