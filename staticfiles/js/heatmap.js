const mapElement = document.getElementById("map");

const stadiaApiKey = mapElement.dataset.stadiaApiKey;

const reports = JSON.parse(mapElement.dataset.reports);


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


const heatData = reports.map(report => [
    report.latitude,
    report.longitude,
    report.risk_score
]);


L.heatLayer(
    heatData,
    {
        radius: 25,
        blur: 15,
        maxZoom: 17
    }
).addTo(map);