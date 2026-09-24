/* jshint esversion: 11 */
const mapElement = document.getElementById("map");

const stadiaApiKey = mapElement.dataset.stadiaApiKey;

const existingLatitude = parseFloat(
    mapElement.dataset.existingLatitude
);

const existingLongitude = parseFloat(
    mapElement.dataset.existingLongitude
);


const defaultLatitude = 52.4862;
const defaultLongitude = -1.8904;


const latitude = Number.isNaN(existingLatitude)
    ? defaultLatitude
    : existingLatitude;

const longitude = Number.isNaN(existingLongitude)
    ? defaultLongitude
    : existingLongitude;


const map = L.map("map").setView(
    [latitude, longitude],
    14
);


L.tileLayer(
    `https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png?api_key=${stadiaApiKey}`,
    {
        maxZoom: 20,

        attribution:
            '&copy; <a href="https://stadiamaps.com/attribution/" target="_blank">Stadia Maps</a> ' +
            '&copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> ' +
            '&copy; <a href="https://www.openstreetmap.org/copyright/" target="_blank">OpenStreetMap</a>'
    }
).addTo(map);


let marker = null;


if (
    !Number.isNaN(existingLatitude) &&
    !Number.isNaN(existingLongitude)
) {

    marker = L.marker([
        existingLatitude,
        existingLongitude
    ]).addTo(map);

}


map.on("click", function (event) {

    const latitude = event.latlng.lat.toFixed(6);
    const longitude = event.latlng.lng.toFixed(6);


    if (marker) {
        map.removeLayer(marker);
    }


    marker = L.marker([
        latitude,
        longitude
    ]).addTo(map);


    document.getElementById("id_latitude").value =
        latitude;

    document.getElementById("id_longitude").value =
        longitude;

});