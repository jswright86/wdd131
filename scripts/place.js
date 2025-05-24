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

const Button = document.querySelector('#text');
const hero = document.querySelector('.hero');

Button.addEventListener('click', () => {
  navigation.classList.toggle('open');
  hamButton.classList.toggle('open');
});

// Add a button to toggle the visibility of the table with class .weather
const weatherTable = document.querySelector('.weather');
const weatherBtn = document.createElement('button');
weatherBtn.textContent = 'Toggle Weather Table';
weatherBtn.id = 'toggleWeatherBtn';

// Insert the button before the weather table
if (weatherTable && weatherTable.parentNode) {
  weatherTable.parentNode.insertBefore(weatherBtn, weatherTable);
  weatherBtn.addEventListener('click', () => {
    weatherTable.classList.toggle('hidden');
  });
}

// Optionally, add a CSS class to hide the table
// .hidden { display: none; }