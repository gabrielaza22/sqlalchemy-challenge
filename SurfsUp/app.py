# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import numpy as np




#################################################
# Database Setup
#################################################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text

# reflect an existing database into a new model
def __init__(self):
    self.engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    self.Base=None
    
    self.init_base()

# reflect the tables
def init_base(self):
    self.Base = automap_base()
    self.Base.prepare(autoload_with=engine)


# Save references to each table
#measurements= Base.classes.measurement
#station=Base.classes.station

# Create our session (link) from Python to the DB
session = Session(self.engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Hi there, this is our Climate Analysis for Honolulu, Hawaii"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start/<end<br/>"
    )

# SQL Queries
@app.route("/api/v1.0/precipitation")
# last 12 months of precipitation data
def query_precipitation(self):

    query = """
            SELECT
                date as Date,
                prcp as Precipitation
            FROM
                measurement
            WHERE
                date >= '2016-08-23'
            
            ORDER BY
                date ASC;
        """
    df = pd.read_sql(text(query), con=self.engine)
    data= df.to_dict(orient='records')
    return(jsonify(data))


