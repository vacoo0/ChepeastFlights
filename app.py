from flask import Flask, render_template, request, session
from datetime import datetime, timedelta
from ryanair import Ryanair
from functions import parse_trip_data, airport_inf, parse_flight_data_one, find_city_id, find_iata_code
import re
from flask import jsonify

import requests

app = Flask(__name__)
app.secret_key = 'dupamarynagrengolada'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search_iata', methods=['POST'])
def search_iata():
    city_name = request.form.get('city_name')
    # Perform the CSV lookup or another logic here to find the IATA code
    iata_code = find_iata_code(city_name)
    response = jsonify(iata_code=iata_code)
    print(response.get_data())  # This will print the response's data in the Flask server console
    return response
@app.route('/search_flights', methods=['POST'])
def search_flights():
    departure = request.form.get('departure')
    # arrival = request.form.get('arrival')
    flight_date = request.form.get('departure_date')  # Fetching the selected date
    flight_date = datetime.strptime(flight_date, "%Y-%m-%d").date()
    departure_flexibility = int(request.form.get('departure_flexibility', 0))
    flight_date_flex = flight_date + timedelta(days=departure_flexibility)

    return_date = request.form.get('return_date')  # Fetching the return date
    return_date = datetime.strptime(return_date, "%Y-%m-%d").date() + timedelta(days=1)
    return_flexibility = int(request.form.get('return_flexibility', 0))
    return_date_flex = return_date + timedelta(days=return_flexibility)

    api = Ryanair(currency="PLN")  # Euro currency, so could also be GBP etc. also

    trips = api.get_cheapest_return_flights(departure, flight_date, flight_date_flex, return_date, return_date_flex)
    print(trips[0])
    parsed_trip = parse_trip_data(str(trips[0]))  # Parse the trip data

    airport_description = airport_inf(departure)
    airport_runways = airport_description.runways
    reviews_url = airport_description.reviews_url
    lat_long_match = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_description))
    latitude = lat_long_match.group(1) if lat_long_match else None
    longitude = lat_long_match.group(2) if lat_long_match else None
    airport_description = str(airport_description).replace("<", "").replace(">", "")
    airport_photos = airport_inf(departure).images.get('thumbnails', [])  # Extract thumbnails

    airport_goal_description = airport_inf(parsed_trip['outbound']['destination'])
    t1 = airport_goal_description.timezone_abbr
    t2 = airport_goal_description.timezone_abbr_name
    t3 = airport_goal_description.timezone_name
    t4 = airport_goal_description.timezone_offset_hours
    time_zone = [t1, t2, t3, t4]
    airport_goal_runways = airport_goal_description.runways
    reviews_url_goal = airport_goal_description.reviews_url
    lat_long_match_goal = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_goal_description))
    latitude_goal = lat_long_match_goal.group(1) if lat_long_match else None
    longitude_goal = lat_long_match_goal.group(2) if lat_long_match else None
    airport_goal_description = str(airport_goal_description).replace("<", "").replace(">", "")
    airport_photos_goal = airport_inf(parsed_trip['outbound']['destination']).images.get('thumbnails', [])  # Extract thumbnails


    id_from = find_city_id(parsed_trip['outbound']['originFull'].split(',')[0])
    print(parsed_trip['outbound']['originFull'].split(',')[0])
    print(id_from)

    id_to = find_city_id(parsed_trip['outbound']['destinationFull'].split(',')[0])
    print(parsed_trip['outbound']['destinationFull'].split(',')[0])
    print(id_to)


    # Render a template with the flight data or handle it as needed
    return render_template('flights.html', flights=parsed_trip, airport=airport_description, airport_goal=airport_goal_description, latlong=[latitude, longitude],
                           latlong_goal=[latitude_goal, longitude_goal], photos=airport_photos, photos_goal=airport_photos_goal, runways=airport_runways,
                           runways_goal=airport_goal_runways, reviews_url_goal=reviews_url_goal, reviews_url=reviews_url, id_from=id_from, id_to=id_to, time_zone=time_zone)

@app.route('/flight_info', methods=['POST'])
def flight_info():
    departure = request.form.get('departure_one')
    api = Ryanair(currency="PLN")  # Euro currency, so could also be GBP etc. also
    tomorrow = datetime.today().date() + timedelta(days=1)

    flight = str(api.get_cheapest_flights(departure, tomorrow, tomorrow + timedelta(days=1))[0])
    parsed_trip = parse_flight_data_one(flight)

    airport_description = airport_inf(departure)
    airport_photos = airport_description.images.get('thumbnails', [])
    reviews_url = airport_description.reviews_url
    airport_runways = airport_description.runways
    lat_long_match = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_description))
    latitude = lat_long_match.group(1) if lat_long_match else None
    longitude = lat_long_match.group(2) if lat_long_match else None
    airport_description = str(airport_description).replace("<", "").replace(">", "")


    airport_goal_description = airport_inf(parsed_trip['destination'])
    t1 = airport_goal_description.timezone_abbr
    t2 = airport_goal_description.timezone_abbr_name
    t3 = airport_goal_description.timezone_name
    t4 = airport_goal_description.timezone_offset_hours
    time_zone = [t1, t2, t3, t4]
    airport_photos_goal = airport_goal_description.images.get('thumbnails', [])
    reviews_url_goal = airport_goal_description.reviews_url
    airport_goal_runways = airport_goal_description.runways
    lat_long_match_goal = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_goal_description))
    latitude_goal = lat_long_match_goal.group(1) if lat_long_match else None
    longitude_goal = lat_long_match_goal.group(2) if lat_long_match else None
    airport_goal_description = str(airport_goal_description).replace("<", "").replace(">", "")


    id_from = find_city_id(parsed_trip['originFull'].split(',')[0])
    print(parsed_trip['originFull'].split(',')[0])
    print(id_from)

    id_to = find_city_id(parsed_trip['destinationFull'].split(',')[0])
    print(parsed_trip['destinationFull'].split(',')[0])
    print(id_to)



    return render_template('flights.html', flights=parsed_trip, airport=airport_description, airport_goal=airport_goal_description,
                           latlong=[latitude, longitude], latlong_goal=[latitude_goal, longitude_goal], photos=airport_photos, photos_goal=airport_photos_goal,
                           runways=airport_runways, runways_goal=airport_goal_runways, reviews_url_goal=reviews_url_goal, reviews_url=reviews_url, id_from=id_from, id_to=id_to, time_zone=time_zone)


@app.route('/departure_info')
def departure_info():
    departure = session.get('airport_from', 'Not set')
    airport_description = airport_inf(departure)
    lat_long_match = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_description))
    latitude = lat_long_match.group(1) if lat_long_match else None
    longitude = lat_long_match.group(2) if lat_long_match else None
    airport_description = str(airport_description).replace("<", "").replace(">", "")
    airport_photos = airport_inf(departure).images.get('thumbnails', [])  # Extract thumbnails
    return render_template('departure_info.html', airport_data=airport_description, photos=airport_photos, latlong=[latitude, longitude])

@app.route('/destination_info')
def destination_info():
    departure = session.get('airport_to', 'Not set')
    print(departure)
    airport_description = airport_inf(departure)
    lat_long_match = re.search(r"Latitude: ([-\d.]+) - Longitude: ([-\d.]+)", str(airport_description))
    latitude = lat_long_match.group(1) if lat_long_match else None
    longitude = lat_long_match.group(2) if lat_long_match else None
    airport_description = str(airport_description).replace("<", "").replace(">", "")

    airport_photos = airport_inf(departure).images.get('thumbnails', [])  # Extract thumbnails
    return render_template('destination_info.html', airport_data=airport_description, photos=airport_photos, latlong=[latitude, longitude])



if __name__ == '__main__':
    app.run(debug=True)
