document.addEventListener('DOMContentLoaded', (event) => {
    VANTA.BIRDS({
        el: "body",
        backgroundColor: "rgba(0,0,0,0)", // Transparent background for birds
        color1: 0x0,
        color2: 0x244855,
        // Other Vanta.js settings
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 600.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        birdSize: 1.40,
        wingSpan: 20.00,
        separation: 50.00,
        alignment: 20.00,
        cohesion: 20.00,
        quantity: 4.00,
        backgroundAlpha: 0.65
    });

});

function searchIata() {
    const cityName = document.getElementById('cityNameInput').value;
    fetch('/search_iata', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'city_name=' + encodeURIComponent(cityName)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();  // This parses the JSON response
    })
    .then(data => {
        // Ensure that you are accessing the 'iata_code' correctly
        document.getElementById('iataResult').textContent = 'IATA Code: ' + data.iata_code;
    })
    .catch(error => {
        document.getElementById('iataResult').textContent = error.message;
    });
}

