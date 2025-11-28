from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, engine


#setting up connection

load_dotenv()

DB_USER = os.getenv("MY_USERNAME")
DB_PASSWORD = os.getenv("MY_PASSWORD")
DB_HOST = os.getenv("MY_HOST")
DB_PORT = os.getenv("MY_PORT")
DB_NAME = os.getenv("MY_DBNAME")

try:
    engine = create_engine("postgres+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo = True)
    Base = declarative_base()
except ConnectionError:
    print("Connection failed. Please cheeck your .env variables again. Also check if you have imported all modules")


# Write csvs to sql

Session = sessionmaker(bind = engine)
session = Session()

#reading in data
# I must name the columns according to my field names

field_names_co2 = ["id", "country_id", "year", "annual_co2_emissions"]
field_names_energy = ["id", "country_id", "year", "primary_energy_consumption"]
field_names_air = ["id", "country_id", "year", "nitrogen",
                   "sulfur_dioxide", "carbon_monoxide",
                   "black_carbon", "ammonia", "non_methane_organic"]

co2_data = pd.read_csv("../Data_processed/cleaned_co2_data.csv")
energy_data = pd.read_csv("../Data_processed/cleaned_energy_data.csv")
air_data = pd.read_csv("../Data_processed/cleaned_air_data.csv")

co2_data.columns = field_names_co2
energy_data.columns = field_names_energy
air_data.columns = field_names_air







