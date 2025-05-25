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
