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

console.log(localStorage.getItem("reviewSubmit")); // Debugging output

document.getElementById("reviewSubmit").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent form submission

    const product = document.getElementById("product").value;
    const rating = document.querySelector('input[name="rating"]:checked').value;
    const review = document.getElementById("review").value;

    if (product && rating && review) {
        const reviewData = {
            product: product,
            rating: rating,
            review: review
        };

        localStorage.setItem("reviewSubmit", JSON.stringify(reviewData));
        console.log("Review submitted:", reviewData); // Debugging output
        alert("Review submitted successfully!");
    } else {
        alert("Please fill out all fields before submitting.");
    }
});