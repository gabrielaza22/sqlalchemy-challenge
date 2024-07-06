# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql= SQLHelper()


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Hi there, this is our Climate Analysis for Honolulu, Hawaii<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
    )

# SQL Queries
@app.route("/api/v1.0/precipitation")
# last 12 months of precipitation data
def query_precipitation():
    data= sql.query_precipitation()
    return(jsonify(data))

@app.route("/api/v1.0/stations")
# last 12 months of precipitation data
def query_stations():
    data= sql.query_stations()
    return(jsonify(data))


@app.route("/api/v1.0/tobs")
# last 12 months of precipitation data
def query_tobs():
    data= sql.query_tobs()
    return(jsonify(data))


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
