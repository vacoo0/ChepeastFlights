
# LLM challenge - chepeast airline tickets
**Authors:** Michał Spinczyk, Piotr Pustelnik, Jan Mrożek

This project is a web application built using the Flask framework in Python, designed to provide a comprehensive service for finding and displaying flight information, specifically utilizing the Ryanair API. The core functionality of the app includes searching for IATA codes, finding the cheapest flights, and gathering detailed information about airports, flights, and destinations. Below is a detailed description of the various components and features of this project:
* Flask Web Framework:
The application is built using Flask, a lightweight and flexible Python web framework. Flask is used for handling HTTP requests, rendering templates, and managing sessions.
* Flight Information Retrieval:
The app integrates with the Ryanair API to fetch flight data. This includes finding the cheapest return and one-way flights, as well as providing flexibility in terms of departure and return dates.
### Airport and Flight Data Processing:
The application includes several custom functions like parse_trip_data, airport_inf, parse_flight_data_one, find_city_id, and find_iata_code for processing and extracting useful information from the data obtained from the API and other sources.
### Regular Expressions for Data Extraction:
Regular expressions are utilized to extract specific pieces of data, such as latitude and longitude, from the airport information.
### Session Management and Routes:
Flask’s session management is used to store and retrieve data like departure and destination airports. Various routes (@app.route) handle different functionalities like searching for IATA codes, fetching flight information, and displaying airport details.
### Dynamic Content Rendering:
The application uses Flask's render_template function to dynamically generate HTML pages. Information about flights, airports, and other related data is passed to templates, allowing for dynamic content display based on user input and API responses.
### Front-End Interactivity:
The front-end interactivity, primarily handled through HTML forms, allows users to input data such as city names, departure dates, and flexibility options, which the back-end processes to fetch and display relevant flight information.
### Security and Debugging:
The application sets a secret key for secure session management. Debug mode is enabled for development purposes, facilitating easier troubleshooting and debugging.
### Application Structure:
The project is structured to separate concerns: routing and logic handling in the main application file, separate modules for specific functionalities (like ryanair.py for API interactions), and HTML templates for the front end.
### Geographical and Time Zone Information:
The application also processes geographical data like latitude and longitude, and time zone information for airports, enhancing the utility of the flight information provided.

In summary, this Flask-based web application serves as a comprehensive tool for users to search for flights, find IATA codes, and access detailed information about airports and destinations, leveraging the Ryanair API and custom Python functions for data processing and presentation.

====================================================================
## Steps:
### Initial Setup and Basic Flask Application:
Developed a basic Flask web application structure.
Created app.py with Flask routes and views.
Set up HTML templates (index.html, flights.html) for different pages.
### Flight Search Feature:
Implemented forms in index.html for users to input flight search criteria.
Created a route in app.py to handle flight search requests, interacting with the Ryanair API to fetch flight data.
Parsed and displayed flight data in flights.html.
### Airport Information and Flexibility Options:
Added options for departure and return date flexibility.
Included an API call to fetch detailed information about the departure airport, displaying it in the flight results.
### Map Integration:
Integrated Leaflet.js for dynamic map rendering, displaying the locations of departure and destination airports.
### Weather Widget:
Integrated OpenWeatherMap widget to display the current weather at the departure and destination locations.
### Time Zone and Airport Runway Information:
Displayed time zone information for the departure and destination airports.
Added a section to show detailed runway information for the airports.
### Styling and Responsive Design:
Developed CSS styles (style.css) for the website to enhance the visual presentation.
Ensured the website is responsive and mobile-friendly.
### Additional Features and Enhancements:
Added a feature to search for one-way flights.
Implemented airport review links and airport photo galleries.
Introduced a JavaScript-based pop-up alert for time zone differences.
### JavaScript Interactivity:
Added JavaScript code to handle interactive elements like the airport information toggle and the IATA code search functionality.
### Data Handling and Error Checks:
Implemented error handling and data validation for form submissions and API responses.
### Backend Data Processing:
Wrote Python functions in app.py for data parsing, API interactions, and utility tasks.
### Deployment and Testing:
Conducted thorough testing of the website features.
Made adjustments and bug fixes based on test results.
### Code Refinement and Documentation:
Refactored code for better readability and performance.
Added comments and documentation throughout the code for clarity.
This project encompassed a full-stack web development process, involving both frontend and backend work, API integration, data processing, and UI/UX design. The website offers a user-friendly interface for searching flights, viewing detailed airport information, and accessing useful features like weather updates and timezone alerts.

====================================================================

### How we started:
- create a nice looking (aircraft style) website on flask where we will use aviation stack api to get information about flights, create two blocks on webpage : 1. where we look flights input(departure place, arrival place) 2. where we et information about flights input(flights number)

### All prompts:
- https://chat.openai.com/share/0aabd2a5-f8ac-48da-89ba-102a893fbf17
- prompts.txt file


