# Orla Higgins, 2018-05-03
# Find the minimum value in a given column

# https://stackoverflow.com/questions/35329573/finding-max-value-in-a-column-of-csv-file-python


# import csv module for streamlined functions
import csv 

# use with function to open, close and manipulate file  
# move to next line of csv file when next piece of data is blank in case there are errors in csv file
with open('iris.csv', newline='') as f:
    
    # csv.reader will iterate over lines in iris.csv
    reader = csv.reader(f)

    # next(reader)       (if you wanted to skip header row)
   
    # columns is csv file are seperated by a comma
    # float is decimal number 
    answer = min(float(column[1].replace(',', '')) for column in reader)
    
    print("The minimum sepal width of any given iris is", answer,"cm")  
    # note column[4] will give an error as it not a numberical value column

