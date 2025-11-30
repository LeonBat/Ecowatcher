#!/usr/bin/env python
# coding: utf-8

# <h1 style = "text-align:center; text-decoration: underline"> Preprocessing of environmental data </h1>

# <i>Libraries</i>

# In[ ]:


import pandas as pd
import os


# <hr>
# <i>Variables and Paths<i>

# In[ ]:


###### Variables
co2_data_path = os.path.join("../Data_raw/annual-co2-emissions-per-country.csv")
energy_data_path = os.path.join("../Data_raw/per-capita-energy-use.csv")
air_data_path = os.path.join("../Data_raw/long-run-air-pollution.csv")

# Reading in data
co2_data = pd.read_csv(co2_data_path)
energy_data = pd.read_csv(energy_data_path)
air_data = pd.read_csv(air_data_path)


# <hr>
# <i>Function definitions</i>

# In[ ]:


#Function for inspecting the datafiles
def inspect_data(input_file: pd.DataFrame) -> None:
    '''
    The function inspect_data expects a pandas DataFrame as input and prints the 
    dimensions, structure and variables of the DataFrame.

    Parameters:
    - input_file: pd.DataFrame

    Returns:
    - None

    >>> inspect_data(co2_data)
    Structure of co2_data dataframe
    '''

    #prints dimensions of dataframe
    print(f"Shape of {input_file} dataframe")
    input_file.shape

    #prints structure of dataframe
    print(f"Info of {input_file} dataframe")
    input_file.info()

    #prints the first 5 rows of dataframe
    print(f"Head of {input_file} dataframe")
    input_file.head(n = 5)


# <hr>
# <b>Inspection<b>

# In[ ]:


inspect_data(co2_data)


# In[ ]:


inspect_data(air_data)


# In[ ]:


inspect_data(energy_data)


# I noticed that in **co2_data** and **energy_data** there are duplicate columns namely **time** and **year**.
# 
# I will remove on of them, to keep the dataframe simpler
# 
# Although in **energy_data** the decision becomes clearer because **year_column** is the same as **time** but with missing values for 2023.

# In[ ]:


co2_data.columns


# In[ ]:


# Dropping duplicate columns
co2_data = co2_data.drop(columns = ["time"])

energy_data = energy_data.drop(columns = ["Year"])
# Rename time column to year
energy_data = energy_data.rename(columns = {"time": "Year"})


# In[ ]:


co2_data.head(n = 5)


# In[ ]:


energy_data.head(n = 5)


# Creation of additional countries table

# In[ ]:


countries = pd.DataFrame()
countries = air_data[["Entity", "Code"]].drop_duplicates()
countries = countries.rename(columns = {"Entity": "name", "Code": "code"})
countries["id"] = range(1, len(countries) + 1)
#place id colunn first
countries = countries[["id", "name", "code"]]
countries.head(n = 5)


# In[ ]:


get_ipython().system('jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace preprocessing.ipynb')
get_ipython().system('jupyter nbconvert --to script preprocessing.ipynb')




# Saving files in Data_processed folder       

# In[ ]:


# Saving path to Data_processed folder
saving_path = "../Data_processed/"

#save cleaned data
co2_data.to_csv(os.path.join(saving_path, "cleaned_co2_data.csv"), index = False)
energy_data.to_csv(os.path.join(saving_path, "cleaned_energy_data.csv"), index = False)
air_data.to_csv(os.path.join(saving_path, "cleaned_air_data.csv"), index = False)
countries.to_csv(os.path.join(saving_path, "countries.csv"), index = False)

