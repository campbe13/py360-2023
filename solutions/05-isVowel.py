# isVowel() 
'''
the function isVowel() takes a letter as a parameter,
returns True if 
'''
# no variable, using or 
def isVowel3(letter): 
  return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or  letter == 'u' or letter == 'i' or letter == 'y'
# variable, using or 
def isVowel2(letter): 
  if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or  letter == 'u' or letter == 'i' or letter == 'y':
    vowel = True
  else:
    vowel = False
  return vowel
# variable
def isVowel(letter):
  if letter == 'a':
    vowel = True
  elif letter == 'e':
    vowel = True
  elif letter == 'i':
    vowel = True
  elif letter == 'o':
    vowel = True
  elif letter == 'u':
    vowel = True
  elif letter == 'y':
    vowel = True  
  else:
    vowel = False
  return vowel

print("a ", isVowel3('a'))
print("e ", isVowel3('e'))
print("i ", isVowel3('i'))
print("o ", isVowel3('o'))
print("u ", isVowel3('u'))
print("y ", isVowel3('y'))
print("f ", isVowel3('f'))

# Using it  with if
letter = 'a'
if isVowel(letter) :
  print(f'letter {letter} is a vowel.')
else:
  print(f'letter {letter} is a NOT vowel.')
