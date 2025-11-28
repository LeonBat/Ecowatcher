############
# DATABASE CREATION SCRIPT
############

#This script is used to create the initial database structure
#for the project.

# Libraries
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


#loading variables from .env file
load_dotenv()

#Importing variables from environment
DB_USER = os.getenv("MY_USERNAME")
DB_PASSWORD = os.getenv("MY_PASSWORD")
DB_HOST = os.getenv("MY_HOST")
DB_PORT = os.getenv("MY_PORT")
DB_NAME = os.getenv("MY_DBNAME")

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise SystemExit("Set DB_USER, DB_PASSWORD and DB_NAME environment variables before running.")
    


# Connect to postgres database
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo = True)
Base = declarative_base()

# Define tables
class Countries(Base):
    __tablename__ = "countries"

    country_id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    code = Column(String, nullable = False, unique = True) 

    co2_table = relationship("CO2", back_populates= "country")
    energy_table = relationship("Energy", back_populates = "country")
    air_table = relationship("Air", back_populates = "country")


class CO2(Base):
    __tablename__ = "co2"

    id = Column(Integer, primary_key = True)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    year = Column(Integer, nullable = False)
    annual_co2_emmissions = Column(Float)

    country = relationship("Countries", back_populates="co2_table")

class Energy(Base):
    __tablename__ = "energy"

    id = Column(Integer, primary_key = True)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    year = Column(Integer, nullable = False)
    primary_energy_consumption = Column(Float)

    country = relationship("Countries", back_populates = "energy_table")

class Air(Base):
    __tablename__ = "air"

    id = Column(Integer, primary_key = True)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    year = Column(Integer, nullable = False)
    nitrogen = Column(Float)
    sulfur_dioxide = Column(Float)
    carbon_monoxide = Column(Float)
    black_carbon = Column(Float)
    ammonia = Column(Float)
    non_methane_organic = Column(Float)

    country = relationship("Countries", back_populates = "air_table")


# Create tables in the database
Base.metadata.create_all(engine)

# Test the connection and table creation
Session = sessionmaker(bind=engine)
session = Session()

# Query to check if tables are created
query = session.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
for table in query:
    print(table)

# Close the session
session.close()
#close connection
engine.dispose()






