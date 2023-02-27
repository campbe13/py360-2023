
# learning about lists & for
# together

'''
given a type of pet return the sound it makes 
parameter string type of pet
return string sound
'''
def animal_sounds(pet):
  if pet == "dog":
    sound = "woof"
  elif pet == "cat":
    sound = "meow"
  elif pet == "mouse":
    sound = "squeak"
  elif pet == "elephant":
    sound = "trumpet"
  else:
    sound = "oink"
  return sound

def main(): 
  # some lists for you to use
  students = ['Jon', 'Jane', 'Jo']
  grades=[80, 65, 97, 44, 100, 44]
  cegeps  \
      = ['Dawson', 'Vanier', 'JAC', 'Gerald Godin', \
         'Champlain', 'dawson College', 'Rosemont']
  fruits = ['apple','banana','cherry','orange', 'kiwi', 'melon', 'orange', 'mango']
  for pet in ["dog", "cat", "mouse", "elephant", "robot"]:
    print(f"{pet} says {animal_sounds(pet)}")
    
  print(fruits, len(fruits))
  del fruits[4]
  print(fruits, len(fruits))
  fruits[3]  = "dragonfruit"
  print(fruits, len(fruits))
  # print(students + fruits+ grades)
  print (grades, len(grades))
  grades.append(99)
  print (grades, len(grades))
  grades.insert(2, 99)
  print (grades, len(grades))
  ix = grades.index(44)
  grades[ix]   = 60
  print (grades, len(grades), ix)
  grades.pop(ix)    # del grades[ix]
  print (grades, len(grades), ix)
  grades.pop()     # del grades[-1]
  print (grades, len(grades))
  
  # pet = 'dog'
  print(f'your {pet} says {animal_sounds(pet)}')
  subset = fruits[3:6]  #3,4,5
  print(subset)
  leng = len(fruits)
  subset = fruits[3:leng+1]  # up to but not including upper range
  print(subset)
  for i in range(len(students)): 
    print(i, students[i])
    
  for student in students:
    if student == 'Jon':
          print("hi Jon")
    print(student)

  if 'Jon' in students:
    print("hi Jon")
  else:
    print ("no Jon")
  
# Code below ensures that the function called main is the entry point 
if __name__ == "__main__":
    main()
