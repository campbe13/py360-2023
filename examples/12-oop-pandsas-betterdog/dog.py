'''
defines the BetterDog class

Improvement on the original Dog class, for use with a dataset
(no age given in the dataset)
'''

class BetterDog:
  # initializer
  def __init__ (self, name,  breed, size, age, sex, breedable, colour):
    # init attributes
    self.name = name # str
    self.breed = breed   # str
    self.size = size  #str
    self.sex = sex  # str
    self.colour = colour  # str
    self.canbreed = breedable # bool
    self.age =  age  # int
  # behaviours
  def bark(self):
    if self.size in ['small','medium']:
      return 'yip yip yip'
    elif self.size == 'xlarge':
      return 'ROWF ROWF RO`WF'
    else:
      return 'rowf rowf rowf'
  def changeAge(self, newage):
    if newage < 0 or newage > 25:
      return
    self.age = newage
  def isBreedable(self):
    return self.canbreed
  def __str__(self):
    return (f"Name {self.name.title()} breed {self.breed.capitalize()} {self.size} {self.colour}")
