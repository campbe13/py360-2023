'''
description here
'''

class Rectangle:
  # add init for attributes & methods (functions) for behaviours  
  def __init__(self, width,height):
    self.width = width
    self.height  = height
  def area(self):
    return self.width*self.height
  def perimiter(self):
    return self.width*2 + self.height*2
  def change(self, width, height):
    if self.width + width >= 0 and \
        self.height + height >= 0:
          self.width += width
          self.height += height
  def __str__(self):
    return f'rectangle width {self.width} height {self.height}'
      
class Square(Rectangle):
    def __init__(self, side):
      self.width = side
      self.height = side
