'''
defines the Dog class
and the Terrier class that inherits from Dog
'''

class Dog:
  # initializer
  # self is a reference to the current instance 
  # only has meanning when we instantiate the opbject
  # is unique to the instance 
  def __init__ (self, name, age, breed, size):
    # init attributes
    self.name = name
    self.age = age
    self.breed = breed
    self.size = size
  # str dunder (double underline) method
  # __str__ used when obj is printed
  def __str__(self):
    return f'{self.name} is a {self.breed}, {self.age} years old'   
  # behaviours
  # all instances have these 
  def bark(self):
    if self.size in ['small','medium']:
      return 'yap yap yap'
    elif self.size == 'xlarge':
      return 'ROWF ROWF ROWF'
    else:
      return 'bark bark bark'
  def isPuppy(self):
    if self.age < 2:
       return True
    return False  
  def change_age(self, factor):
    self.age += factor
# inherit from Dog
class Terrier(Dog):
  def __init__ (self, name, age):
    # init attributes
    self.name = name
    self.age = age
    self.breed = 'Terrier'
    self.size = 'small'
  # override bark
  def bark(self):
      return 'Terrer yip yip yip'
  # own methods (not in Dog / parent class)
  def trouble(self):
    if self.age < 5:
      return ("****")
    else: 
      return ("**")
