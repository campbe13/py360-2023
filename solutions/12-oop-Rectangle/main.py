'''
use the Rectangle class
pmcampbell
2023-05-01
'''
from Rectangle import *

def main():
  lot = Square(100)
  house = Rectangle(40,30)
  dog_house = Rectangle(2,4)
  driveway = Rectangle(5,8)
  area_to_mow = lot.area() - house.area() - dog_house.area() - driveway.area()
  print('lot', lot, lot.area(), 'area to mow', area_to_mow)
  # testing change
  lot.change(5, 15)
  print('lot after change', lot, lot.area())
if __name__ == '__main__':
  main()
