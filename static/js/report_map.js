const mapElement = document.getElementById("map");

const stadiaApiKey = mapElement.dataset.stadiaApiKey;


const map = L.map("map").setView(
    [52.4862, -1.8904],
    12
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


let marker;


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


    document.getElementById("id_latitude").value = latitude;

    document.getElementById("id_longitude").value = longitude;

});