# Instructions  

  **pandas is powerful when you want to manipulate existing datasets**

  _we will work with csv (comma separated value) files_

  Note: we rely on pandas functions to read the file (and encapsulate some error handling), we do not have to open and read them ourselves as you did in assignment 2.
  
  ## References
  * *Look at the slide deck for pandas*  there are some more explanations & actions for this dataset
  * https://realpython.com/pandas-python-explore-dataset/
  * https://realpython.com/pandas-plot-python/
 ## Steps - basics
  Note the path to file depends on where you are running your code for repl.it (you have to upload the file to repl it to use it, I supplied it here)
 ![upload csv](assets/upload-csv.jpg)
  1. download the csv file shown in the image, have a look at the data  (it is easier to see the structure using excel)
  1. read a csv file `df = pd.read_csv('assets/recent-grads.csv')`  
  3. examine the content  `dv.head()` `df.tail()` `df.shape()` etc
  4. datatypes of the columns `df.info()`
  5. basic statistics `df.describe()`   `df.Median`
  6. Try a few stats methods from the pandas intro tutorial, ex what are the minimum numbers of Women in any program, Men?

 ## Using the file 
 The file contains  174 the first row is the headers; so all other rows are 173 unique majors (open the file to see the data)
 In order to analyse and ask questions about data you must understand the content 
 1.  count values   / occurrences of values `df.Major_category.value_counts()`
 2. expore the dataset ; filter the dataframe where a condition is met (median starting salaries for engineering)  note *Major_category*  try a few <br>`eng_mean = df[df.Major_category == 'Engineering'].Median.mean()` 
 3.  count the majors  in Biology & Life Science  `df[df.Major_category == 'Biology & Life Science'].Major.value_counts()`
 4. use dataframe loc method (same result) `df.loc[df.Major_category == 'Biology & Life Science', 'Major'].value_counts()`
5. highest median salaray for Engineering  (try a few others, or lowest) <br>`highest_med = df.[ df.Major_category == 'Engineering'].Median.max()`
6. try a few more queries

## plotting 
Try a few plots, create a function

1.  add `import matplotlib.pyplot as plt` <br> You can give `df.plot()` arguments that define the values plotted on x and y 
3. try the following `df.plot(x="Rank", y=["Men", "Women"])`
4. then plot y as the 25th and 75th percentile by Rank
5. then plot y as the Median by Rank
6. Try a different x value for the preceeding (ex Major_category)
7. Look at the slides, try a few plots from there
