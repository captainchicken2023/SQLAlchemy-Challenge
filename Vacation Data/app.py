# Import the dependencies.
import numpy as np
import datetime as dt

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
    return (
        f"Hawaii Climate API: Welcome<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/Precipitation<br/>"
        f"/api/v1.0/Stations<br/>"
        f"/api/v1.0/TOBS<br/>"
        f"/api/v1.0/Starting%20Temps<br/>"
        f"/api/v1.0/Starting%20Ending%20Temps<br/>"
    )


@app.route("/api/v1.0/precipitation")
def Precipitation():
    session = Session(engine)





# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
query1 = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= prior_year).all()

prp_query = session.query(measurement.date, measurement.prcp).\
                 filter(measurement.date >= prior_year).all()


session.close()

# Return the JSON representation of your dictionary.
    prp_dict = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(prp_dict)

# @app.route("/api/v1.0/stations")
#     def Stations():
    # session = Session(engine)

# # Return a JSON list of stations from the dataset.
    # return()


# @app.route("/api/v1.0/tobs")
#     def TOBS():
    # session = Session(engine)

# # Query the dates and temperature observations of the most-active station for the previous year of data.

# # Return a JSON list of temperature observations for the previous year.
    # return()


# @app.route("/api/v1.0/<start>")
#     def Starting_Temps():
    # session = Session(engine)

# # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    # return()

# # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

  

# @app.route("/api/v1.0/<start>/<end>")
#     def Starting_Ending_Temps():
    # session = Session(engine)

# # For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.







if __name__ == "__main__":
    app.run(debug=True)





# # Hints
# # Join the station and measurement tables for some of the queries.

# # Use the Flask jsonify function to convert your API data to a valid JSON response object.



# #A start route that:

# #Accepts the start date as a parameter from the URL (2 points)

# #Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)



# #A start/end route that:

# #Accepts the start and end dates as parameters from the URL (3 points)

# #Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)