# Orla Higgins, 2018-05-03
# Make a histogram using iris data set
# Plots a simple histogram of sepal lengths of iris set

# https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
# https://zahidhasan.github.io/2017-04-13-ploting-with-seaborn/

# import libraries for streamlined functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv 

# load csv file into pandas
df = pd.read_csv('iris.csv')

# assign column attributes in pandas, [0,1,2,3]
df.columns = ['sepal-len','sepal-wd','petal-len','petal-wd','species']

# use Seaborn/matplotlib to generate a visualisation of the data
plt.hist(df['species'])

# print/display
plt.show()

plt.hist(df['sepal-len'])
plt.show()
