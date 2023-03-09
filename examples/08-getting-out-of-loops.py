# it is best to structure your code to end a loop properly / naturally 
# however
# you can use break and continue to jump out of loops in exceptional circumstances
'''    
I want to tell you if the letter 'a' is in a word without using the in operator
Since this is a function, you can return as soon as you find the answer
'''
def find_a(word):
   for letter in word:
      if letter == 'a':
          return True
   # end of loop, been through all the letters
   return False
'''
I want to tell you where I found the letter 'a' by printing something to the screen
once I find a I get out of the loop 
'''
def show_where_a(word):
  index= -1
  for i in range(len(word)):
    if word[i].lower() == 'a' :
        index = i
        break
      
  if (index < 0):
    print('no a')
  else:
    print(f'Found a at {index}:  {word[index]}') 
    

'''    
I want to print everything in the string except  spaces 
try this with everything except a,e,i,o and u
'''
def no_spaces(word):
   for letter in word:
      if letter == ' ':
          continue
      print(letter)
''' 
challenge, copy the code from no_spaces() to no_char below 
change it to not print the given char
no_char(word, 't') #print everything but t
'''
def no_char(word, char_omit):
  pass  #remove this it's a placeholder
  
def main():
  if find_a("nothing to see here but a"):
    print("found a")
  else:
    print("did not find a")
          
  if find_a("nothing to see here but..."):
    print("found a")
  else:
    print("did not find a")
    
  show_where_a("nothing to see here but...")
  show_where_a("nothing to see here but a")

  no_spaces("nothing to see here but ...")
  
if __name__ == '__main__':
  main()
