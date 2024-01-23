# LLM Challenge - Cheapest Airline Tickets
## Creators
- Michał Spinczyk
- Piotr Pustelnik
- Jan Mrożek

## Project Overview
This project is a web application using the Flask framework in Python, aimed at providing a comprehensive service for finding and displaying flight information. It utilizes the Ryanair API for its core functionalities.

### Flask Web Framework
- Utilizes Flask for handling HTTP requests, rendering templates, and session management.

### Flight Information Retrieval
- Integrates with the Ryanair API.
- Finds the cheapest return and one-way flights.
- Provides flexibility in departure and return dates.

### Airport and Flight Data Processing
- Custom functions: `parse_trip_data`, `airport_inf`, `parse_flight_data_one`, `find_city_id`, `find_iata_code`.
- Processes data from the API and other sources.

### Regular Expressions for Data Extraction
- Uses regex to extract data like latitude and longitude from airport information.

### Session Management and Routes
- Uses Flask’s session management.
- Routes (`@app.route`) for functionalities like IATA code search and flight information fetching.

### Dynamic Content Rendering
- Uses Flask's `render_template` function for HTML pages.
- Dynamic content based on user input and API responses.

### Front-End Interactivity
- HTML forms for user input.
- Processes input for relevant flight information.

### Security and Debugging
- Secret key for session management.
- Debug mode for development and troubleshooting.

### Application Structure
- Separation of concerns: routing/logic handling, API interactions, and HTML templates.

### Geographical and Time Zone Information
- Processes geographical data and time zone information for airports.

## Development Steps

### Initial Setup and Basic Flask Application
- Basic Flask web application structure.
- `app.py` with routes and views.
- HTML templates: `index.html`, `flights.html`.

### Flight Search Feature
- Forms in `index.html` for flight search criteria.
- Route in `app.py` for flight search requests.
- Flight data parsing and display in `flights.html`.

### Airport Information and Flexibility Options
- Departure and return date flexibility.
- API call for departure airport information.

### Map Integration
- Leaflet.js for dynamic map rendering.

### Weather Widget
- OpenWeatherMap widget for current weather at locations.

### Time Zone and Airport Runway Information
- Time zone information display.
- Runway information section.

### Styling and Responsive Design
- CSS styles (`style.css`) for visual presentation.
- Responsive and mobile-friendly design.

### Additional Features and Enhancements
- One-way flights search feature.
- Airport review links and photo galleries.
- JavaScript-based time zone difference alert.

### JavaScript Interactivity
- Interactive elements handling.

### Data Handling and Error Checks
- Error handling and data validation.

### Backend Data Processing
- Python functions for data parsing and utility tasks.

### Deployment and Testing
- Website feature testing and adjustments.

### Code Refinement and Documentation
- Code refactoring and commenting.

## Starting the Project
- Aim: A nice-looking (aircraft style) Flask website.
- Use the Aviation Stack API for flight information.
- Two webpage blocks: 1. Flight input (departure, arrival) 2. Flight information (flight number).

## Resources
- Project Prompts: [OpenAI Chat Link](https://chat.openai.com/share/0aabd2a5-f8ac-48da-89ba-102a893fbf17)
- Prompts file: `prompts.txt`
