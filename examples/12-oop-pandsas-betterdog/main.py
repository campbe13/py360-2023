'''
using Dog License data with  pandas
instantinating and using objects from the BetterDog class
'''
from dogs import BetterDog
import pandas as pd

'''
BetterDog attributes on instantiation
name,  breed, size, age, sex, breedable, colour
'''
def buildDog(random_dog):
  colour = random_dog.Color
  name = random_dog.DogName
  breed = random_dog.Breed
  size = random_dog.Size
  sex = ''
  breedable = False
  if 'female' in random_dog.LicenseType.lower():
    sex = 'female'
    if 'spayed' in random_dog.LicenseType.lower():
      breedable = False
    else:
      breedable = True
  elif 'male' in random_dog.LicenseType.lower():
    sex = 'male'
    if 'neutered' in random_dog.LicenseType.lower():
      breedable = False
    else:
      breedable = True
  
  first_dog = BetterDog(name,breed,size, 0, sex, breedable, colour)
  return first_dog
def dog_stats(dogdf):
  dogdf.info()
  # show the first few rows of the dataframe
  print(dogdf.head())
  print(dogdf.tail())  # last
  # show breed info
  dogdf.Breed
  print(dogdf.Breed.value_counts())

  ### which is the most common breed (largest count)
  print(dogdf.Breed.value_counts())
  print("most common", dogdf.Breed.value_counts().max())
  print("most common",  dogdf['Breed'].value_counts().idxmax())
  ### which is the most common name
  print("most common name")
  print("name", dogdf.DogName.value_counts().max())
  print("name",  dogdf.DogName.value_counts().idxmax())  # not an index because data is string
  ### which is least common name
  print("least common", dogdf.DogName.value_counts().min())
  print("least common",  dogdf['DogName'].value_counts().idxmin())

  breed_series = dogdf.Breed.value_counts() 
  # go throught the series  & show breeds with only 1 
  for breed, count in breed_series.items():
    if count <= 1:
      print(breed)

  single_breed = []
  for breed, count in breed_series.items():
    if count <= 1:
      single_breed.append(breed)

  print("only 1", single_breed)

def main():
  dogdf = pd.read_csv('dogs2017.csv')
  dog_stats(dogdf)
  
  '''
  create some better dog objects
  first extract some data
  '''
  list_of_dogs = []
  for i in range(5):
    #random_dog = dogdf.sample() # need ref iloc[0] on random_dog
    random_dog = dogdf.sample().reset_index().iloc[0]
    adog = buildDog(random_dog)
    list_of_dogs.append(adog)

  for dog in list_of_dogs:
    print(dog, dog.bark())

if __name__ == '__main__':
  main()
