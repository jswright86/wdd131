
let temp = document.getElementById("temp1").textContent;
let winds = document.getElementById("wind1").textContent;
let temperature = parseFloat(temp);
let windSpeed = parseFloat(winds);
let windchill = '';


function calcWindchill(temperature, windSpeed, id) {
    // Calculate wind chill using the formula
    id = document.getElementById(id).textContent;
   
    if (temperature <= 50 && windSpeed >= 3) {
        windchill =
        Math.round(35.74 + (0.6215 * temperature) - (35.75 * Math.pow(windSpeed, 0.16)) + (0.4275 * temperature * Math.pow(windSpeed, 0.16))) 
        
        return document.getElementById("wc1").textContent = windchill + "°F";
    } else {
        return "N/A";
    }
}
calcWindchill(temperature, windSpeed ,"wc1");

let northwest = {
    Temp: '45 °F',
    Wind: '10 mph',
    WindChill: calcWindchill(45, 10, "wc1"),
    Condition: 'Sunny',};
let southwest = {
    Temp: '60 °F',
    Wind: '15 mph',
    WindChill: calcWindchill(60, 15, "wc1"),
    Condition: 'Cloudy',};

function sectiontemplate(section) {
    return northwest};

function renderSections(northwest) {
    let section = document.getElementById("sections");
    section.innerHTML = `
        <h2>Northwest Section</h2>
        <p>Temperature: ${northwest.Temp}</p>
        <p>Wind Speed: ${northwest.Wind}</p>
        <p>Wind Chill: ${northwest.WindChill}</p>
        <p>Condition: ${northwest.Condition}</p>
    `;
}