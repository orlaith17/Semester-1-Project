# Orla Higgins, 2018-05-03
# Find the average of a given column in a csv file dataset
# using numpy library

# https://stackoverflow.com/questions/49970309/how-do-i-calculate-the-mean-of-each-species-of-the-iris-data-set-in-python

# import libraries for streamlined functions
# numpy code has not been shortened to np in this instance
import numpy 

# read data file into array
data = numpy.genfromtxt('iris.csv', delimiter=',')

# pick the first column of data and define first column
meanfirstcol = numpy.mean(data[:,0])
print("Mean of sepal length is:", meanfirstcol)

# pick the second column of data and define second column
meansecondcol = numpy.mean(data[:,1])
print("Mean of sepal width is:", meansecondcol)

# pick the third column of data and define third column
meanthirdcol = numpy.mean(data[:,2])
print("Mean of petal length is:", meanthirdcol)

# pick the fourth column of data and define fourth column
meanfourthcol = numpy.mean(data[:,3])
print("Mean of petal width is:", meanfourthcol)

# note column[4] will give an error as it not a numberical value column