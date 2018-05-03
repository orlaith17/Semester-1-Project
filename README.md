# Semester-1-Project    
---------------------  


## README.md Contents  
### 1. Summary of Repository Contents
### 2. Summary of Iris Dataset
### 3. Summary of Investigations    
  
## Repository Contents 
File Name | Content
------------ | ------------- 
  README.md | Text file containting summary of project investigations 
  irishisto.py | File containing Python code that will plot a simple histogram of the sepal lengths in the iris dataset
  irismax.py | File containing Python code that will find the max value in a given column of the iris dataset
  irismean.py | File containing Python code that will find the mean value in a given column of the iris dataset
  irismin.py | File containing Python code that will find the minimum value in a given column of the iris dataset
  irisscatter.py | File containing Python code that will map variables of the iris dataset via a scatterplot visualisation
  irissum.py | File containing Python code that will find the sum value of a given column of the iris dataset
  iris.csv | Isis data set in csv file format. This was the dataset file used to run with the Python coded files
  R_Fisher.gif | Image 01 used in README.md
  LICENCE | 
  .gitignore |  

   


  



## Summary of the Iris Dataset
In the era of Richard Dawkins, Ronald Fischer was a biostatistician driven by data associated with hereditary and natural selection including the ‘sexy son hypothesis’. He was a strong supporter of eugenics which post-WWII is probably an unpopular belief/practice. Despite this, his methodologies mean that he was one of the leading contributors to modern statistical science. 

<p align="center">
  <img width="700" height="auto" src="https://github.com/orlaith17/Semester-1-Project/blob/master/R_Fisher.gif?raw=true">
</p>

Edward Anderson’s 1935 collection of data on the irises of the Gaspé Peninsula records the attributes of 150 irises under 5 attributes - petal length, petal width, sepal length, sepal width and class. Anderson used 50 samples of three different species of irises; Iris setosa, Iris versicolor, and Iris virginica. Based on the data collected by Anderson, Fischer produced the paper, ‘The Use of Multiple Measurements in Taxonomic Problems’.

In the 1936 paper, he developed a linear discriminant method to distinguish species from each other using a linear combination of features that separates or characterises two or more classes. Through the linear discriminant method, Fisher theorised that the probability of misclassification based on the plotted variables is significantly reduced. 

The linear discriminant model became a classic multivariate data set. The term “multivariate statistics” is appropriately used to include all statistics where there are more than two variables simultaneously analysed. The application of the iris data is used on support vector machines for machine testing algorithms. It is less likely to be used in cluster analysis since two of the three iris class cluster together. This makes the iris data set a good example of distinguishing between supervised and unsupervised data mining. 

Supervised data mining techniques are used when you have a specific target value you’d like to predict about your data. Unsupervised data mining does not focus on predetermined attributes, nor does it predict a target value. Rather, unsupervised data mining finds hidden structure and relation among data.

http://archive.ics.uci.edu/ml/datasets/Iris list a number of noteworthy papers which have since cited the data set and the link http://lab.fs.uni-lj.si/lasin/wp/IMIT_files/neural/doc/seminar8.pdf describes an experiment in which the data set was used to demonstrate three different neural network architectures. 
### References
* https://en.wikipedia.org/wiki/Iris_flower_data_set  
* https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x  
* https://en.wikipedia.org/wiki/Ronald_Fisher  
* https://stats.stackexchange.com/questions/201359/what-were-the-main-statistical-contributions-of-ronald-fisher  
* http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf  
* http://rstudio-pubs-static.s3.amazonaws.com/269829_8285925c922e445097f47925b112841f.html  
* https://www.apsl.net/blog/2017/07/18/using-linear-discriminant-analysis-lda-data-explore-step-step/  
* https://en.wikipedia.org/wiki/Support_vector_machine  
* http://core.ecu.edu/psyc/wuenschk/MV/IntroMV.pdf  
* https://cloudtweaks.com/2014/09/use-supervised-unsupervised-data-mining/  
* http://archive.ics.uci.edu/ml/datasets/Iris  
* http://lab.fs.uni-lj.si/lasin/wp/IMIT_files/neural/doc/seminar8.pdf  
* https://www.kaggle.com/benhamner/sepal-width-vs-length/code  


## Summary of Investigations  
### Plotting a simple histogram of the sepal lengths
#### Method  
- Importation of streamlined libraries  
- load csv in pandas
- assign column attributes in pandas  
- use Seaborn/matplotlib to generate a visualisation of the data as below. 
#### Result
- Historgram identifies that most iris sepal lengths are 4.5-7cm

<p align="center">
  <img width="500" height="auto" src="https://github.com/orlaith17/Semester-1-Project/blob/master/Histogram.png?raw=true">
</p>

### Plotting a scattermap based on three variables
#### Method  
- Importation of streamlined libraries  
- load csv in pandas
- assign column attributes in pandas  
- use Seaborn/matplotlib to generate a visualisation of the data as below. Plot sepal length vs. petal length and assign hue to the iris species.   
#### Result
- Scattermap identifies two clusters on the map with Iris-setosa clearly distinguished from the other two species based on petal and sepal length.  

<p align="center">
  <img width="500" height="auto" src="https://github.com/orlaith17/Semester-1-Project/blob/master/Scattermap.png?raw=true">
</p>

### Finding the max value in a given column
#### Method  
- import csv module for streamlined functions
- use with function to open, close and manipulate file  
- csv.reader will iterate over lines in iris.csv
- use max function for a given column. Columns in CSV are seperated by a comma and a decimal placed number is identified as a float. note the fifth column will give an error as it not a numberical value column
#### Result
- Code returns that the maximum petal length of a given iris is 6.9cm.  

### Finding the mean value in a given column
#### Method - Using numpy library  
- import libraries for streamlined functions
- read data file into array
- select a given column of data and define column
- apply numpy.mean function and print
- repeat for other columns. Note the fifth column will give an error as it not a numberical value column
#### Result
- Code returns: 
  - mean of sepal length: 5.84333333333
  - mean of sepal width is: 3.054
  - mean of petal length is: 3.75866666667
  - mean of petal width is: 1.19866666667 
  
  
### Finding the min value in a given column  
#### Method - Using numpy library  
- import csv module for streamlined functions
- use with function to open, close and manipulate file 
- csv.reader will iterate over lines in iris.csv
- use min function for a given column. Columns in CSV are seperated by a comma and a decimal placed number is identified as a float. note the fifth column will give an error as it not a numberical value column  
#### Result
- Code returns that the minimum sepal width of any given iris is 2.0 cm. 

### Finding the sum value of a given column  
#### Method 1 - Using numpy library  
- import libraries for streamlined functions
- read data file into array
- select a given column of data and define column
- apply numpy.sum function and print
- repeat for other columns. Note the fifth column will give an error as it not a numberical value column

#### Method 2 
- import csv module for streamlined functions
- use with function to open, close and manipulate file  
- move to next line of csv file when next piece of data is blank in case there are errors in csv file
- set variable
- create a for loop using the i_add function 
- csv.reader will iterate over lines in iris.csv
  
#### Result
- Code returns slight variation between the two methods - Method 1; the total sum of the first column is 876.5, Method 2; the total sum of the first column is 876.5000000000002. I would determine that there is an error in Method 2, although after testing the code, I haven't quite understood what is causing the issue. 





