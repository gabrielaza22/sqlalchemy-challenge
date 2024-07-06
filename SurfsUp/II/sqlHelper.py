import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text


import pandas as pd
import numpy as np

class SQLHelper():
    
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)


    def query_precipitation(self):

            # Query all passengers
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

        df = pd.read_sql(text(query), con = self.engine)
        data = df.to_dict(orient="records")
        return(data)

    def query_stations(self):
        query = """
                SELECT 
                    station
                FROM
                    measurement

            """

        df2 = pd.read_sql(text(query), con= self.engine)
        data2 = df2.to_dict(orient="records")
        return(data2)


    def query_tobs(self):
        query = """
                SELECT 
                    tobs
                FROM
                    measurement
                WHERE
                    date >= '2016-08-23'
                AND station= 'USC00519281'
            """
        df3 = pd.read_sql(text(query), con=self.engine)
        data3 = df3.to_dict(orient="records")
        return(data3)

