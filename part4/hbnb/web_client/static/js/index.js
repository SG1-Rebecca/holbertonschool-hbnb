/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {

    checkAuthentication();

    function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        // Fetch places data if the user is authenticated
        fetchPlaces(token);
    }
}
function getCookie(name) {
    // Function to get a cookie value by its name
    const cookie = document.cookie
}

/* Fetch places data */

async function fetchPlaces(token) {
    // Make a GET request to fetch places data
    try {
        const url = 'http://localhost:3000/api/places'
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        });

        const data = await response.json();
        displayPlaces(data);

    } catch (error) {
        console.error('Error', error);
        
    }
    // Include the token in the Authorization header
    // Handle the response and pass the data to displayPlaces function
}

function displayPlaces(places) {
    // Clear the current content of the places list
    const placeList = document.getElementById('places-list');
    placeList.innerHTML = '';
    // Iterate over the places data
    // For each place, create a div element and set its content
    places.forEach(place => {
        const div = document.createElement('div');
        div.classList.add('place-content');

        div.dataset.price = place.price;

        div.innerHTML = `
            <h3><strong>${place.name}</strong></h3>
            <p>${place.description}</p>
            <p>${place.price}</p>
            <p>${place.location}</p>
            <button>View details</button>`;
        // Append the created element to the places list
        placeList.append(div);
    });
}

/* Filter  */

document.getElementById('price-filter').addEventListener('change', (event) => {
    // Get the selected price value
    // Iterate over the places and show/hide them based on the selected price
    const selectedPrice = event.target.value;
    const options = document.querySelectorAll('.place-content');

    let maxPrice;
    switch (selectedPrice) {
        case "10":
            maxPrice = 10;
            break;
        case "50":
            maxPrice = 50;
            break;
        case "100":
            maxPrice = 100;
            break;
        case "all":
        default:
            maxPrice = Infinity; // Price with no filter
            break;
    }

    options.forEach(option => {
            const price = parseFloat(option.getAttribute('data-price'));
            /* Display price */
            if (price <= maxPrice) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
    });
    
});
  });