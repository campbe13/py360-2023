# reading from csv files
# create dicts
# pmcampbell
# 2023-03-13

import csv

def read_from_csv(file_name):
  # Open the file by calling open and then use csv.DictReader.
  with open(file_name) as a_file:
    reader = csv.DictReader(a_file)
    for row in reader:
        print (row)

def csv_to_dict_list(file_name):
  list = []
  with open(file_name) as a_file:
    reader = csv.DictReader(a_file)
    for row in reader:
        list.append (row)
  return list
'''
given a list of dicts, find the oldest 'age' 
assumes the dicts in the list have a name key and an age key
parameter list of dicts
returns age and name of oldest
'''
def find_oldest(list):
    age = 0
    name = None
    for entry in list:
      if 'age' in entry and 'name'  in entry:
        entry_age = int(entry['age'])
        if age < entry_age:
          age = entry_age
          name = entry['name']
    return age, name 
          
      # check if age & name keys  exist 

#  get the data 


def main():
  read_from_csv('dogs.csv')
  # with open('cats.csv') as catfile:
  #   reader = csv.DictReader(catfile)
  #   print(reader)
  #   count = 1
  #   for row in reader:
  #       print (count, row)
  #       count += 1 
  read_from_csv('cats.csv')
  cat_list = csv_to_dict_list('cats.csv')
  print(cat_list)
  age,name = find_oldest(cat_list)
  # 0 is a sentinal that 
  if (age,name) == (0,None):  
      print('no cats or data is bad (negative ages)')
  print(f'oldest cat is {name}, age {age}')
  # use the list
  for cat_dict in cat_list:
    if float(cat_dict['weight']) >=11:
      print(f"{cat_dict['name']} is overweight ")

# Code below ensures that the function called main is the entry point 
if __name__ == "__main__":
    main()
