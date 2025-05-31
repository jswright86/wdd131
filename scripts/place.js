let year = document.querySelector("#year");
let today = new Date();
year.innerHTML = `<span class="highlight">${today.getFullYear()}</span>`;
let oLastModif = new Date(document.lastModified);
let nLastModif = new Date(document.lastModified).getTime();
lastModified.innerHTML = `Last Modification: <span class="highlight">${oLastModif.toLocaleDateString("en-US", {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
})}</span> ${oLastModif.toLocaleTimeString("en-US", {
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
})}`;

const calculateWindChill = (temp, speed) => {
  if (temp <= 50 && speed > 3) {
    return Math.round(
      35.74 + 0.6215 * temp - 35.75 * Math.pow(speed, 0.16) + 0.4275 * temp * Math.pow(speed, 0.16)
    );
  } else {
    return "N/A";
  }
}
let calculateWindChillDisplay = () => {
  let temp = parseFloat(document.querySelector("#temp").textContent = "70"); // Default temperature for demonstration
  let speed = parseFloat(document.querySelector("#speed").textContent = "5"); // Default speed for demonstration
  let windChill = calculateWindChill(temp, speed);
  document.querySelector("#windchill").textContent = windChill;
} 
// Update the wind chill display when the page loads

const westButton = document.getElementById('west');
westButton.addEventListener('click', function() {
  const westWeather = document.createElement("tbody");
  westWeather.innerHTML = '<tr><td>Temperature: 70F</td><td>Conditions: Sunny</td><td>Wind: 5 mph</td><td>Humidity: 65%</td></tr>';
  // Replace 'th' with the actual table element you want to append to, e.g.:
  const table = document.querySelector("#your-table-id"); // Change to your table's id or selector
  if (table) {
    table.appendChild(westWeather);
  }
});


let names = ['Nancy','Blessing','Jorge','Svetlana','Bob'];
let namesLength = names.map(name => name.length);
console.log(namesLength); // [5, 8, 5, 8, 3]