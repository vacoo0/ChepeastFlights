import re
from datetime import datetime
from FlightRadar24 import FlightRadar24API
import json

def parse_trip_data(trip_str):
    # Regular expression patterns for extracting data
    flight_pattern = r"Flight\(departureTime=datetime\.datetime\((.*?)\), flightNumber='(.*?)', price=(.*?), currency='(.*?)', origin='(.*?)', originFull='(.*?)', destination='(.*?)', destinationFull='(.*?)'\)"
    trip_pattern = r"Trip\(totalPrice=(.*?), outbound=" + flight_pattern + ", inbound=" + flight_pattern + "\)"

    def parse_datetime(datetime_str):
        # Attempt to parse datetime with different formats
        for fmt in ('%Y-%m-%d-%H-%M', '%Y-%m-%d-%H-%M-%S', '%Y-%d-%m-%H-%M', '%Y-%d-%m-%H-%M-%S'):
            try:
                return datetime.strptime(datetime_str.replace(', ', '-'), fmt)
            except ValueError:
                continue
        raise ValueError(f"Unable to parse date-time: {datetime_str}")

    match = re.search(trip_pattern, trip_str)
    if match:
        return {
            "totalPrice": float(match.group(1)),
            "outbound": {
                "departureTime": parse_datetime(match.group(2)),
                "flightNumber": match.group(3),
                "price": float(match.group(4)),
                "currency": match.group(5),
                "origin": match.group(6),
                "originFull": match.group(7),
                "destination": match.group(8),
                "destinationFull": match.group(9)
            },
            "inbound": {
                "departureTime": parse_datetime(match.group(10)),
                "flightNumber": match.group(11),
                "price": float(match.group(12)),
                "currency": match.group(13),
                "origin": match.group(14),
                "originFull": match.group(15),
                "destination": match.group(16),
                "destinationFull": match.group(17)
            }
        }
    else:
        return {"error": "Unable to parse trip data"}



import csv

def find_iata_code(city_name):
    iata_code = None
    with open('iata-icao.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['region_name'].lower() == city_name.lower():
                iata_code = row['iata']
                break
    return iata_code
def parse_flight_data_one(flight_data_str):
    # Define a regular expression pattern to extract flight details
    pattern = r"departureTime=datetime\.datetime\((\d{4}), (\d{1,2}), (\d{1,2}), (\d{1,2}), (\d{1,2})\), flightNumber='(.*?)', price=(.*?), currency='(.*?)', origin='(.*?)', originFull='(.*?)', destination='(.*?)', destinationFull='(.*?)'"

    # Search for the pattern in the flight data string
    match = re.search(pattern, flight_data_str)
    if match:
        # Extract and construct the flight details
        departure_time = datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)),
                                  int(match.group(5)))
        flight_details = {
            'departureTime': departure_time.strftime("%Y-%m-%d %H:%M"),
            'flightNumber': match.group(6),
            'price': float(match.group(7)),
            'currency': match.group(8),
            'origin': match.group(9),
            'originFull': match.group(10),
            'destination': match.group(11),
            'destinationFull': match.group(12)
        }
        return flight_details
    else:
        return {'error': 'Unable to parse flight data'}

def airport_inf(airport_name):
    fr_api = FlightRadar24API()
    airport = fr_api.get_airport(code=str(airport_name), details=True)
    return airport

def find_city_id(city_name, country_code=None):
    # Load city list
    with open('city.list.json', encoding='utf-8') as file:
        cities = json.load(file)

    # Search for the city
    for city in cities:
        if city['name'].lower() == city_name.lower() and (country_code is None or city['country'] == country_code):
            return city['id']

    return "City not found"