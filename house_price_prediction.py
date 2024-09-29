#Import Libraries:

#import pandas as pd: Imports the pandas library and assigns it the alias pd, which is used for data manipulation and analysis.
#import matplotlib.pyplot as plt: Imports the pyplot module from the matplotlib library and assigns it the alias plt, which is used for creating static, animated, and interactive visualizations.
#import seaborn as sns: Imports the seaborn library and assigns it the alias sns, which is used for making statistical graphics.
#import os: Imports the os module, which provides a way of using operating system-dependent functionality like reading or writing to the file system.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Print Current Working Directory:
#os.getcwd(): Gets the current working directory.

print("Current Working Directory:", os.getcwd()) #Prints the current working directory to the console

# Load the dataset from the .xlsx file
dataset = pd.read_excel('data/datasets/Housing_Data.xlsx', engine='openpyxl') #Reads an Excel file into a pandas DataFrame using the openpyxl engine.

# Explore the dataset

print(dataset.head(10)) #Returns the first 10 rows of the DataFrame.

dataset.shape #Returns a tuple representing the dimensionality of the DataFrame (number of rows and columns).

##Identify Categorical Variables:

#dataset.dtypes == 'object':
# #Creates a boolean Series indicating which columns have the data type ‘object’ (typically used for categorical data).

#obj = (dataset.dtypes == 'object'):
# #Assigns this boolean Series to the variable obj.

#obj[obj].index:
# #Selects the indices (column names) where the value is True.

#object_cols = list(obj[obj].index):
# #Converts these indices to a list and assigns it to object_cols.

obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables:",len(object_cols)) #Prints the number of categorical variables.


int_ = (dataset.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables:",len(num_cols))

fl = (dataset.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables:",len(fl_cols))



###

# Select numerical columns
numerical_dataset = dataset.select_dtypes(include=['number'])

# Print the numerical dataset to verify
print(numerical_dataset.head())

# Create and display the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(numerical_dataset.corr(),
            cmap='BrBG',
            fmt='.2f',
            linewidths=2,
            annot=True)
plt.show()

