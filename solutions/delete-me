# For strings see also 07-strings-for.py
# this is based on 07-strings-for instructions
# THIS IS A TEMPLATE, REPLACE WHAT IS NEEDED
# description  
# name
# date

# import statments

# functions
'''
function description (1 each)
'''
'''best solution'''
def secondletters(word):
  secondstring = ''
  # best solution
  for ix  in range(0, len(word), 2):
     #print(word[ix], ix) # debug
     secondstring += word[ix]
  return secondstring
  
'''good solution'''
def secondletters2(word):
  secondstring = ''
  for ix  in range(len(word)):
    if ix%2 == 0:
      secondstring += word[ix]
  return secondstring
'''  
ok, not great, avoid using continue
used here as an example
'''
def secondletters3(word):
  secondstring = ''
  for ix  in range(len(word)):
    if ix%2 != 0:
      print(ix)
      continue
    secondstring += word[ix]
  return secondstring

'''
using slices, string has blank delimited words 1st & last name 
'''
def slicing1():
  name= "Greta Thunberg"
  # starts at 0
  # end not included (like range)
  # a slice   [start:end]
  part = name[4:8]
  print (len(part), part)     # chars 4-7
  print (name[8:])      # start at 8th char to end
  print (name[:5])      # first 5 chars
  # not good code, here for examples of using break & continue
  for ix in range(len(name)):
    if name[ix] != ' ':
      continue
    last_name = name[ix+1:] 
    first_name = name[:ix]
    break
  return first_name, last_name
  
def slicing2():
  name="Nic Olas"
  # starts at 0
  # end not included (like range)
  # a slice   [start:end]
  part = name[4:8]
  print (len(part), part)     # chars 4-7
  print (name[8:])      # start at 8th char to end
  print (name[:5])      # first 5 chars
  
  #better than slicing1()
  for ix in range(len(name)):
    if name[ix] == ' ':
      last_name = name[ix+1:] 
      first_name = name[:ix]
      break
  return first_name, last_name
  
# main() function
def main():
  sentence = "the quick brown fox"
  print(len(sentence))
  print (secondletters(sentence))
  print (secondletters2(sentence))
  print (secondletters3(sentence))
  print ("\nslicing-----------------\n")
  first_name,last_name = slicing1()
  print(f'first {first_name} last {last_name}')
  first_name,last_name = slicing2()
  print(f'first {first_name} last {last_name}')
  
if __name__ == '__main__':
    main()
