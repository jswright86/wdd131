
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


const products = [
    {
        id: "SG-st01",
        name: "Steel-Frame Safty Glasses",
    },
    {
        id: "SG-st02",
        name: "Steel-Frame Safty Glasses with UV Protection",
    },
    {
        id: "SG-pl01",
        name: "Plastic-Frame Safty Glasses",
    },
    {
        id: "SG-pl02",
        name: "Plastic-Frame Safty Glasses with UV Protection",
    },
    {
        id: "SG-rb01",
        name: "Rubber-Frame Safty Glasses",
    },
    {
        id: "SG-rb02",
        name: "Rubber-Frame Safty Glasses with UV Protection",
    }
];

populateProducts(products);

function populateProducts(products) {
    products.forEach(product => {
        const option = document.createElement("option");
        option.value = product.name;
        option.textContent = product.name;
        document.getElementById("product").appendChild(option);
    })
};



document.getElementById('submit').addEventListener('click', function(event) {
    // Prevent any default form submission
    event.preventDefault();
    
    if (validateForm()) {
        submitReview();
    }
});

function validateForm() {
    const requiredInputs = document.querySelectorAll('input[required]');
    
    const allRequiredFilled = Array.from(requiredInputs).every(input => {
        return input.value.trim() !== '';
    });
    
    if (!allRequiredFilled) {
        alert('Please complete all required fields that are marked with an asterisk (*) before submitting.');
        return false;
    }
    
    return true;
}

function submitReview() {
    // Increment review count
    let numReviews = Number(localStorage.getItem("reviewSubmit")) || 0;
    numReviews++;
    localStorage.setItem("reviewSubmit", numReviews);
    
    // Success actions
    alert('Review submitted successfully!');
    console.log(`Total reviews submitted: ${numReviews}`);
   
}
    
