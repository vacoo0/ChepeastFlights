var departureMap;
var destinationMap;

function toggleInfo(airportType, lat, lon, photos) {
    var departureInfo = document.getElementById('departureInfo');
    var destinationInfo = document.getElementById('destinationInfo');

    if (airportType === 'departure') {
        departureInfo.style.display = 'block';
        destinationInfo.style.display = 'none';
        if (!departureMap) {
            setTimeout(function () {
                departureMap = initDepartureMap(lat, lon);
            }, 400);
        } else {
            setTimeout(function () {
                departureMap.invalidateSize();
            }, 400);
        }

    } else if (airportType === 'destination') {
        departureInfo.style.display = 'none';
        destinationInfo.style.display = 'block';
        if (!destinationMap) {
            setTimeout(function () {
                destinationMap = initDestinationMap(lat, lon);
            }, 400);
        } else {
            setTimeout(function () {
                destinationMap.invalidateSize();
            }, 400);
        }
    }
}

function initDepartureMap(latitude, longitude) {
    var map = L.map('departure-map').setView([latitude, longitude], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.marker([latitude, longitude]).addTo(map).bindPopup("<b>Departure Airport Location</b>").openPopup();
    return map;
}

function initDestinationMap(latitude, longitude) {
    var map = L.map('destination-map').setView([latitude, longitude], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.marker([latitude, longitude]).addTo(map).bindPopup("<b>Destination Airport Location</b>").openPopup();
    return map;
}

$(document).ready(function () {
    // Your jQuery code
    $('#destinationInfo').hide();
});


