# exercises for 08-using-dicts
# teacher's solutions

'''
write a function create_triples() 
that creates a dict containing powers of 3, up to 10 return the dict. ex {0:0, 1:3, 2:9... 10:59049} hint use for Challenge: instead of 10 use a parameter as the maximum
'''
def create_triples(max):
  triples = {0:0}
  for power in range(1, max + 1):
    triples[power] = 3**power
  return triples
'''
Write a function count_letters() that takes a string as a parameter count the vowels (aeiou,y) in the string and return a dict with those counts. ex {a:2,i:0...}.
'''
def count_letters(phrase):
  count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
  for letter in phrase:
    if letter == 'a':
      count['a'] += 1
    elif letter == 'e':
      count['e'] += 1
    elif letter == 'i':
      count['i'] += 1
    elif letter == 'o':
      count['o'] += 1
    elif letter == 'u':
      count['u'] += 1
    elif letter == 'y':
      count['y'] += 1
  return count
''' alternate solution '''
def count_letters2(phrase):
  count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
  for letter in phrase:
    if letter == 'a' or  letter == 'e' or letter == 'i'  or letter == 'o'  \
       or letter == 'u' or letter == 'y':
         count[letter] += 1
  return count

'''
Write a function begin_end() that takes a string and a letter as parameters. It checks if the letter is at the beginning or end of the letter, then constructs a dict to return. ex: begin_end('python is great', 'p') would return {'begin':True ,'end':False.}
'''
def begin_end(phrase, letter):
  result = {'begin':False ,'end':False}
  if phrase [0] == letter:
    result['begin'] = True
  if phrase [-1] == letter:
    result['end'] = True
  return result
'''
write a function make_dict() that takes as a parameter a list and returns a dict. The list can have any length and any values but assume they are unique and the same type. It will use the list values as keys in a dict, and set the value to zero. ex ['apples', cherries'] converted to {'apples':0, 'cherries':0}
'''
def make_dict(keys):
  dict  = {}
  for key in keys:
    dict [key] = 0
  return dict

'''
create a list of grocery 4 items, use make_dict() to create a dictionary from that list Create a function prices() that takes a dict created by make_dict() as a parameter. In the function prompt the user for the price of each of the key items, update the dict. Print the dict before and after you call prices() to see the results Note: prices will not be a single purpose function (we don't usually use input inside a function)
'''
def prices(dict):
  for key in dict.keys():
    dict[key] = float(input(f'Enter the price of {key}: '))

def main():
  print(create_triples(10))
  phrase = "the dog barked y i uu"
  print(phrase, count_letters(phrase))
  print(phrase, count_letters2(phrase))
  phrase = "p at both ends p"
  print(phrase, begin_end(phrase, 'p'))
  phrase = "p begin only"  
  print(phrase, begin_end(phrase, 'p'))
  phrase = "end only p"  
  print(phrase, begin_end(phrase, 'p'))
  phrase = "no p at begin/end"  
  print(phrase, begin_end(phrase, 'p'))
  list = ['apples', 'cherries', 'mangos']
  print(make_dict(list))
  list = [ 60.5, 77.5, 10.0]
  print(make_dict(list))
  list = ['broccoli', 'cherries', 'mangos', 'bread']
  groceries = make_dict(list)
  print('before',groceries)
  prices(groceries)
  # Note: the dict is mutable, we change it in the function  
  # (can do the same with lists)
  print('after',groceries)
  
if __name__ == "__main__":
  main()
