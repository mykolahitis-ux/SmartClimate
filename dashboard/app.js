// Placeholder data until the backend API is available
function getReadings() {
  return { temperature: 23.4, humidity: 48.2, co2: 780 };
}

function render() {
  const r = getReadings();
  document.getElementById("temp").textContent = r.temperature + " °C";
  document.getElementById("hum").textContent = r.humidity + " %";
  document.getElementById("co2").textContent = r.co2 + " ppm";
}

render();
setInterval(render, 5000);
