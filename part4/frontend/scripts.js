/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  // Form Submission
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      // Make the AJAX request to the API:
      async function loginUser (email, password) {
        const url = '/api/v1/auth/login';

        try {
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
          });

          // Handle the response
          if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            // Redirect to the main page
            window.location.href = 'index.html';
          } else {
            const errorData = await response.json();
            alert('Login failed: ' + (errorData.message || response.statusText));
          }
        } catch (error) {
          console.error('Error:', error);
          alert('An error occurred during login. Please try again.');
        }
      }

      // Call the login function with the form data
      await loginUser(email, password);
    });
  }
  populatePriceFilter();
  displayPlaces(mockPlaces);
  /* INDEX */
  // Check authentication status on page load
  checkAuthentication();
});
function checkAuthentication () {
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
async function fetchPlaces (token) {
  // Make a GET request to fetch places data
  const url = '/api/v1/places';
  // Include the token in the Authorization header
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (response.ok) {
      const data = await response.json();
      displayPlaces(data.places);
    } else {
      console.error('Failed to fetch places:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching places:', error);
  }
  // Handle the response and pass the data to displayPlaces function
}
// Populate the price filter dropdown
function populatePriceFilter () {
  const priceFilter = document.getElementById('price-filter');
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
}
const mockPlaces = [
  { id: 1, name: 'Cozy Cottage', price: 50 },
  { id: 2, name: 'Modern Apartment', price: 100 },
  { id: 3, name: 'Beach House', price: 150 }
];
function displayPlaces (places) {
  const placesList = document.getElementById('places-list');
  // Clear the current content of the places list
  placesList.innerHTML = '';
  // Iterate over the places data
  places.forEach(place => {
    // For each place, create a div element and set its content
    const placeItem = document.createElement('div');
    placeItem.className = 'place-item';
    placeItem.setAttribute('data-price', place.price);
    placeItem.innerHTML = `
      <h3>${place.name}</h3>
      <p>Price per night: $${place.price}</p>
      <button onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
    `;
    // Append the created element to the places list
    placesList.appendChild(placeItem);
  });
}
document.getElementById('price-filter').addEventListener('change', (event) => {
  // Get the selected price value
  const selectedPrice = event.target.value;
  // Iterate over the places and show/hide them based on the selected price
  const placeItems = document.querySelectorAll('.place-item');
  placeItems.forEach(item => {
    const price = item.getAttribute('data-price');
    if (selectedPrice === 'all') {
      item.style.display = 'block';
    } else {
      // Compare the price of the place with the selected price
      // Convert the selected price to an integer for comparison
      const maxPrice = parseInt(selectedPrice);
      // Show the place if its price is less than or equal to the selected price
      if (price <= maxPrice) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    }
  });
});
