# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return "Welcome"


#A start route that:

#Accepts the start date as a parameter from the URL (2 points)

#Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)






#A start/end route that:

#Accepts the start and end dates as parameters from the URL (3 points)

#Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)