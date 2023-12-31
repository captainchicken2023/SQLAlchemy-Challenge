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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def Precipitation():
    session = Session(engine)


# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prp_query = session.query(measurement.date, measurement.prcp).\
                    filter(measurement.date >= prior_year).all()


    session.close()

# Return the JSON representation of your dictionary.
    prcp_list = []
    for date, prcp in prp_query:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_list.append(prcp_dict)

    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(station.station, station.name).all()

    session.close()

# Return a JSON list of stations from the dataset.
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_stations = session.query(measurement.station).group_by(measurement.station).order_by(func.count(measurement.id).desc()).first().station

# Query the dates and temperature observations of the most-active station for the previous year of data.
    usc00519281_data = session.query(measurement.date, measurement.tobs).\
        filter_by(station = most_active_stations).\
            filter(measurement.date >= prior_year).all()
    session.close()

# Return a JSON list of temperature observations for the previous year.
    usc00519281_tobs = list(np.ravel(usc00519281_data))
    return jsonify(usc00519281_tobs)

@app.route("/api/v1.0/temp/<start>")
def starting_temps(start):
    session = Session(engine)  
    start_filter=session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).all()
    
    session.close()

# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    temp1_results = list(np.ravel(start_filter))
    return jsonify(temp1_results)  

@app.route("/api/v1.0/temp/<start>/<end>")
def Starting_Ending_Temps(start, end):
    session = Session(engine)
    start_end_filter=session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    session.close()

# # For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    temp2_results = list(np.ravel(start_end_filter))
    return jsonify(temp2_results)  




if __name__ == "__main__":
    app.run(debug=True)
