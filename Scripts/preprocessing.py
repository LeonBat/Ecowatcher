#################################
# Preprocessing Script for data #
#################################

#Libraries
import pandas as pd
import os


###### Variables
co2_data_path = os.path("../Data_raw/annual-co2-emissions-per-country.csv")
energy_data_path = os.path("../Data_raw/per-capita-energy-use.csv")
air_data_path = os.path("../Data_raw/long-run-air-pollution.csv")

# Reading in data
co2_data = pd.read_csv(co2_data_path)
energy_data = pd.read_csv(energy_data_path)
air_data = pd.read_csv(air_data_path)




###### Function definitions

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

    print(f"Shape of {input_file} dataframe")
    input_file.shape

    print(f"Info of {input_file} dataframe")
    input_file.info()

    print(f"Head of {input_file} dataframe")
    input_file.head()


#Function for adding ID columns to the files --> setting up keys for database
def adding_IDs():
    pass






####### Preprocessing