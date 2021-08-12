# %%
"""
# Notebook 1: Data Wrangling(Cleaning) 

Table of Contents:
* [Data Import and its overview](#1) 
* [Data Cleaning](#2)
"""

# %%
# import the libraries
import numpy as np 
import pandas as pd
from tabulate import tabulate # to print pretty dataframe 

# %%
"""
## Data Import and its overview<a id=1></a>  
Data can be imported from kaggle by several ways:  
* Download the data and then import from local
* Import data by Kaggle API
* Read Data through Url(Used this method)
* Read Data by using gcs_path(google cloud service) of kaggle data sets.
"""

# %%
data_url = "https://raw.githubusercontent.com/Gkchandora/Breast_Cancer_Prediction/main/Dataset/Data/wdbc_data.csv"
df = pd.read_csv(data_url)

# %%
# glimpse of data set
df.head()

# %%
#  number of instances and features in data are:
if __name__=="__main__":
    print(f" Total number of instances = {df.shape[0]}\n",
          f"Number of features = {len(df.columns)}\n"
          " ----------------------------------------------------\n"
          f" The features of the data are :\n {df.columns.values}",)

# %%
# data types
df.dtypes.sort_values() # alternate syntax df.info() which gives too much information

# %%
"""
As we can see data types are:
* `id` has `int64`
* `diagnosis` has `object`
* rest all feautures are `float64` data type
"""

# %%
"""
## Data Cleaning<a id=2></a>
"""

# %%
# Inspection of missing data

# Total missing values and column wise missing counts etc
if __name__=="__main__":

    mis_val_count = df.isna().sum(axis = 0)

    # Total missing values in entire data
    print(f"Total missing values = {mis_val_count.sum(axis=0)}")

    # Column with missing counts > 0
    mis_val_col = mis_val_count[mis_val_count>0]
    mis_val_col = pd.DataFrame(mis_val_col, columns = ["# Missing Counts"])
    mis_val_col.index.name = "Features"
    print(tabulate(mis_val_col, headers='keys', tablefmt='psql'))

# %%
# Drop the columns which have no use  : id, Unnamed 32
df.drop(["id", "Unnamed: 32"], inplace = True, axis = 1)

# %%
# change the title of the diagnosis feature
df.rename(columns = {"diagnosis":"target"}, inplace = True)

# %%
# Lets check whether string("?") exist or not in our data, it might be missed in the above approach if it was string type
df[ (df == "?").sum(axis = 1) > 0]

# %%
"""
$\color{red}{\textrm{Note}}$ :  
Care should be taken for the entires in each columns, for example : `radius_mean` should be greater than zero. So, understanding and knowledge of data is necessary to build the model. 
"""

# %%
# Implementation of above mentioned note : Identify data where radius_mean is <= 0 and radius_worst < = 0

df[(df.radius_mean <= 0) & (df.radius_worst <= 0)]


# %%
"""
*Data is cleaned successfully, now let's move to the next step EDA for model builiding.[EDA Notebook]()*
"""