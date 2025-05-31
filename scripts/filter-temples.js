
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

const hamButton = document.querySelector('#menu');
const navigation = document.querySelector('.navigation');

hamButton.addEventListener('click', () => {
	navigation.classList.toggle('open');
	hamButton.classList.toggle('open');
});

const templeCards = document.querySelector('#templeCards');
if (templeCards) {
  templeCards.innerHTML = `Temple Cards: <span class="highlight">8</span>`;
}
const temples = [
  {
    templeName: "Aba Nigeria",
    location: "Aba, Nigeria",
    dedicated: "2005, August, 7",
    area: 11500,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/7210c09be95c4474772ae52e5f31c23c08112784/full/640%2C/0/default"
  },
  {
    templeName: "Manti Utah",
    location: "Manti, Utah, United States",
    dedicated: "1888, May, 21",
    area: 74792,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/d9c313eb96c173d0ad32f21f461ce994129c9e8d/full/640%2C/0/default" 
  },
  {
    templeName: "Payson Utah",
    location: "Payson, Utah, United States",
    dedicated: "2015, June, 7",
    area: 96630,
    imageUrl:
      "https://churchofjesuschrist.org/imgs/595590aa805080f86e63368963860d9f3dfb3bfd/full/640%2C/0/default"
  },
  {
    templeName: "Yigo Guam",
    location: "Yigo, Guam",
    dedicated: "2020, May, 2",
    area: 6861,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/9f541175bcfc11eca77eeeeeac1ea52488fbff2f/full/640%2C/0/default"
  },
  {
    templeName: "Washington D.C.",
    location: "Kensington, Maryland, United States",
    dedicated: "1974, November, 19",
    area: 156558,
    imageUrl:
      "https://churchofjesuschrist.org/imgs/9bbc2a18ee4b11eb90efeeeeac1e68824aabff60/full/640%2C/0/default"
  },
  {
    templeName: "Lima Perú",
    location: "Lima, Perú",
    dedicated: "1986, January, 10",
    area: 9600,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/b800f5245ce311fb987aabd6ee6b2230b7c8b04f/full/640%2C/0/default" 
  },
  {
    templeName: "Mexico City Mexico",
    location: "Mexico City, Mexico",
    dedicated: "1983, December, 2",
    area: 116642,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/2dbb637a01da374959e9b50dd072294645917ea4/full/640%2C/0/default"
  },
  {
    templeName: "Salt Lake City Utah",
    location: "Salt Lake City, Utah, United States",
    dedicated: "1893, April, 6",
    area: 253000,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/92c33bcbf9cf85483e008d6871f8ced5f6d7b661/full/640%2C/0/default"
  },
  {
    templeName: "San Antonio Texas",
    location: "San Antonio, Texas, United States",
    dedicated: "2005, May, 15",
    area: 16800,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/1dc0b8602087f0f95c062dd122dd45e080d25432/full/640%2C/0/default"
  },
  {
    templeName: "San Diego California",
    location: "San Diego, California, United States",
    dedicated: "1993, June, 19",
    area: 72000,
    imageUrl:
      "https://www.churchofjesuschrist.org/imgs/9fc6d53550ed3243fb8eca9ebceb284d4865e7db/full/640%2C/0/default"
  }
];

// Create cards for all temples
createTempleCard(temples);
const oldtemples = document.querySelector('#Old');

  oldtemples.addEventListener('click', () => {
    // Clear existing cards
    
    // Filter and display only old temples (dedicated before 1900)
  // Remove existing cards
  document.querySelector(".res-grid").innerHTML = "";
  // Filter and display only old temples (dedicated before 1900)
  const oldTemples = temples.filter(temple => temple.dedicated.includes('18'));
  createTempleCard(oldTemples);
});
  const newtemples = document.querySelector('#New');

  newtemples.addEventListener('click', () => {

  document.querySelector(".res-grid").innerHTML = "";
  // Filter and display only new temples (dedicated after 2000)
  const newTemples = temples.filter(temple => temple.dedicated.includes('20'));
  createTempleCard(newTemples); 
 });
  const largetemples = document.querySelector('#Large');
  largetemples.addEventListener('click', () => {
    // Clear existing cards
    document.querySelector(".res-grid").innerHTML = "";
    // Filter and display only large temples (area greater than 90,000 sq ft)
    const largeTemples = temples.filter(temple => temple.area > 90000);
    createTempleCard(largeTemples);
  });
  
  const smalltemples = document.querySelector('#Small');
  smalltemples.addEventListener('click', () => {
    // Clear existing cards
    document.querySelector(".res-grid").innerHTML = "";
    // Filter and display only small temples (area less than 10,000 sq ft)
    const smallTemples = temples.filter(temple => temple.area < 10000);
    createTempleCard(smallTemples);
  });
 const hometemples = document.querySelector('#Home');
  hometemples.addEventListener('click', () => {
    // Clear existing cards
    document.querySelector(".res-grid").innerHTML = "";
    // Display all temples
    createTempleCard(temples);
  });
  
  



function createTempleCard(templesArray) {
  templesArray.forEach(temple => {
    let card = document.createElement('section');
    let name = document.createElement('h3');
    let location = document.createElement('p');
    let dedicated = document.createElement('p');
    let area = document.createElement('p');
    let image = document.createElement('img');


    name.textContent = temple.templeName;
    location.innerHTML = `<span class="label">Location:</span> ${temple.location}`;
    dedicated.innerHTML = `<span class="label">Dedicated:</span> ${temple.dedicated}`;
    area.innerHTML = `<span class="label">Size:</span> ${temple.area} sq ft`;
    image.setAttribute('src', temple.imageUrl);
    image.setAttribute('alt', `${temple.templeName} Temple`);
    image.setAttribute('loading', 'lazy');

    card.appendChild(name);
    card.appendChild(location);
    card.appendChild(dedicated);
    card.appendChild(area);
    card.appendChild(image);

    document.querySelector(".res-grid").appendChild(card);
  });
}