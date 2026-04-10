/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

const API_BASE_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
  // Execute the authentication check when the DOM is fully loaded
  checkAuthentication();
  populatePriceFilter();
});

function checkAuthentication () {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    if (loginLink) {
      loginLink.style.display = 'block';
    }
    displayPlaces(mockAvailablePlaces);
  } else {
    loginLink.style.display = 'none';
    // Fetch places data if the user is authenticated
    fetchPlaces(token);
  }
}
function getCookie (name) {
  // Function to get a cookie value by its name
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) {
      return value;
    }
  }
  return null;
}

// ===== Fetch Places Data =====
async function fetchPlaces (token) {
  // Make a GET request to fetch places data
  const url = `${API_BASE_URL}/api/v1/places/`;
  // Include the token in the Authorization header
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    // Handle the response and pass the data to displayPlaces function
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      displayPlaces(Array.isArray(data) ? data : data.places ?? []);
    } else {
      console.error('Failed to fetch places:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching places:', error);
  }
}

function displayPlaces (places) {
  const placesList = document.getElementById('places-list');
  if (placesList) {
    // Clear the current content of the places list
    placesList.innerHTML = '';
    // Iterate over the places data
    // For each place, create a div element and set its content
    places.forEach(place => {
      const placeElement = document.createElement('div');
      placeElement.className = 'place-container';
      placeElement.setAttribute('data-price', place.price);
      placeElement.innerHTML = `
                <h3>${place.title}</h3>
                <p>Price per night: $${place.price}</p>
                <button class="view-details-btn" onclick="viewDetails('${place.id}')">View Details</button>
            `;
      // Append the created element to the places list
      placesList.appendChild(placeElement);
    });
  }
}

function viewDetails (placeId) {
  // Redirect to the place details page once the "View Details" button is clicked
  console.log('Debug PlaceId:', placeId);
  
  window.location.href = `/place?id=${placeId}`;
}

const priceFilter = document.getElementById('price-filter');

if (priceFilter) {
  priceFilter.addEventListener('change', (event) => {
    // Get the selected price value
    const selectedPrice = event.target.value;
    // Iterate over the places and show/hide them based on the selected price
    const placeItems = document.querySelectorAll('.place-container');
    placeItems.forEach(item => {
      const price = item.getAttribute('data-price');
      if (selectedPrice === 'all') {
        item.style.display = 'block';
      } else {
        // Compare the price of the place with the selected price
        // Convert the selected price to an integer for comparison
        const maxPrice = parseInt(selectedPrice);
        // Show the place if its price is less than or equal to the selected price
        if (parseInt(price) <= maxPrice) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      }
    });
  });
}

function populatePriceFilter () {
  const priceFilter = document.getElementById('price-filter');
  if (priceFilter) {
    const options = [
      { value: 'all', label: 'All' },
      { value: '10', label: '10' },
      { value: '50', label: '50' },
      { value: '100', label: '100' }
    ];

    options.forEach(opt => {
      const option = document.createElement('option');
      option.value = opt.value;
      option.textContent = opt.label;
      priceFilter.appendChild(option);
    });
  } else {
    console.error('Price filter element not found');
  }
}

// ===== MOCK DATA =====

const mockAvailablePlaces = [
  { id: 1, title: 'Cozy Cottage', price: 50 },
  { id: 2, title: 'Modern Apartment', price: 100 },
  { id: 3, title: 'Beach House', price: 150 }
];
