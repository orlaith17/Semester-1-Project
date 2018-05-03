# Orla Higgins, 2018-05-03
# Scatter plot using iris data set
# Maps variables on their petal and sepal length via scatterplot visualisation
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
df.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']

# use Seaborn/matplotlib to generate a visualisation of the data
# plot Sepal Length against Petal Length 
# data defined in df = iris.csv
# add hue using the variables in 'Species' column
# i don't want a mean line running through data so i set fit_reg to False
sns.lmplot('Sepal Length', 'Petal Length', data=df, hue='Species', fit_reg=False)

# print/display
plt.show()


