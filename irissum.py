# Orla Higgins, 2018-05-03
# Find the sum of values for a given column in a csv dataset



# using numpy library
# https://stackoverflow.com/questions/49970309/how-do-i-calculate-the-mean-of-each-species-of-the-iris-data-set-in-python
# similar method to getting the mean of a column

# import library for streamlined functions
# numpy code has not been shortened to np in this instance
import numpy

# read data file into array
data = numpy.genfromtxt('iris.csv', delimiter=',')

# pick the first column of data and define sum of first column
sumfirstcol = numpy.sum(data[:,0])

print("The total sum of the first column is", sumfirstcol)



# other method
# https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python?rq=1

# import csv module for streamlined functions
import csv

# use with function to open, close and manipulate file  
# move to next line of csv file when next piece of data is blank in case there are errors in csv file
with open('iris.csv', newline='') as f:
  # set variable
  total = 0
  # create a for loop using the i add function 
  # csv.reader will iterate over lines in iris.csv
  for col in csv.reader(f):
      total += float(col[0])
# I can't figure out here why .000000000002 is also added????
print('The total sum of the first column is', total)



