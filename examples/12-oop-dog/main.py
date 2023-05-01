# use the dog class
from Dog import Dog,Terrier
# from Dog import *

def main():
  blake = Dog('Blake', 4, 'mutt', 'xlarge')
  chico = Dog('Chico', 14, 'poodle', 'small')
  freddie = Dog("Freddie", 6, "wheaton", 'medium')
  baby = Terrier("Tiny", .5 )
  print(freddie) # object
  print(freddie.bark()) # method
  print(freddie.name,freddie.age) # attribute
  # update the object instance
  print(blake.name, blake.age) # attribute
  blake.age +=1  # had a birthday
  print(blake.name, blake.age) # attribute
  print(blake.name, blake.bark()) # attribute
  print(blake.isPuppy())
  if (blake.isPuppy()):
    print(blake.name, "is a puppy")
  else:
    print(blake.name, "is an adult dog")
  print(baby.name, baby.bark())
  if (baby.isPuppy()):
    print(baby.name, "is a puppy")
  print(baby, "trouble factor", baby.trouble())
  print(chico)
  chico.change_age(-5)
  print(chico)

if __name__ == '__main__':
  main()
