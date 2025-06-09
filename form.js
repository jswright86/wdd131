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


let submitCount = 0;

document.getElementById("reviewSubmit").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default submission for demo purposes
    submitCount++;
    console.log("Form submitted", submitCount, "times.");
});
