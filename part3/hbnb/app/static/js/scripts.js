/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
const API_BASE_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const reviewForm = document.getElementById('review-form');

  // Form Submission
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      // Make the AJAX request to the API:
      async function loginUser (email, password) {
        const url = `${API_BASE_URL}/api/v1/auth/login`;

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
  // Review Form Submission
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      // Get review text from form
      const reviewText = document.getElementById('review').value;
      // Make AJAX request to submit review
      async function submitReview (reviewText) {
        const token = getCookie('token');
        const placeId = getPlaceIdFromURL();
        const url = `${API_BASE_URL}/api/v1/places/${placeId}/reviews`;

        try {
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({ comment: reviewText })
          });

          // Handle the response
          if (response.ok) {
            alert('Review submitted successfully!');
            // Optionally, refresh the page or update the reviews section
          } else {
            const errorData = await response.json();
            alert('Failed to submit review: ' + (errorData.message || response.statusText));
          }
        } catch (error) {
          console.error('Error:', error);
          alert('An error occurred while submitting the review. Please try again.');
        }
      }

      // Call the submitReview function with the review text
      await submitReview(reviewText);
    });
  }
  populatePriceFilter();
  displayPlaces(mockPlaces);
  checkAuthentication();
});

// Check authentication status on page load

function checkAuthentication () {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  const addReviewSection = document.getElementById('add-review');
  const placeId = getPlaceIdFromURL(); // Get the place ID from the URL

  // ===== INDEX =====

  if (loginLink) {
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
      // Fetch places data if the user is authenticated
      fetchPlaces(token);
    }
  }
  // ===== PLACES =====
  if (addReviewSection) {
    if (!token) {
      addReviewSection.style.display = 'none';
    } else {
      addReviewSection.style.display = 'block';
      // Fetch place details if the user is authenticated and a place ID is present in the URL
      if (placeId) {
        // Store the token for later use
        fetchPlaceDetails(token, placeId);
      }
    }
  }

  // ===== ADD REVIEW =====
  if (!token) {
    window.location.href = 'index.html';
  }
  return token;
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
  const url = `${API_BASE_URL}/api/v1/places/`;
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
const mockPlaces = [
  { id: 1, name: 'Cozy Cottage', price: 50 },
  { id: 2, name: 'Modern Apartment', price: 100 },
  { id: 3, name: 'Beach House', price: 150 }
];

const mockPlaceDetails = {
  id: 1,
  name: 'Beautiful Beach House',
  price: 150,
  description: 'A beautiful beach house with amazing views...',
  amenities: ['WiFi', 'Pool', 'Air Conditioning'],
  reviews: [
    { user: 'Jane Smith', comment: 'Great place to stay!' },
    { user: 'Robert Brown', comment: 'Amazing location and very comfortable.' }
  ]
};

function displayPlaces (places) {
  const placesList = document.getElementById('places-list');
  if (!placesList) return; // If the places list element is not found, exit the function
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

const priceFilter = document.getElementById('price-filter');

if (priceFilter) {
  priceFilter.addEventListener('change', (event) => {
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
        if (parseInt(price) <= maxPrice) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      }
    });
  });
}

// ===== PLACES DETAILS =====

function getPlaceIdFromURL () {
  // Extract the place ID from window.location.search
  const extractPlaceId = new URLSearchParams(window.location.search);
  // Return the place ID
  return extractPlaceId.get('id');
}

async function fetchPlaceDetails (token, placeId) {
  // Make a GET request to fetch place details
  const url = `${API_BASE_URL}/api/v1/places/${placeId}`;
  // Include the token in the Authorization header
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
      // Handle the response and pass the data to displayPlaceDetails function
    if (response.ok) {
      const data = await response.json();
      displayPlaceDetails(data);
    } else {
      console.error('Failed to fetch place details:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching place details:', error);
  }
}

function displayPlaceDetails (place) {
  console.log('Displaying place details', place);

  const placeDetailsSection = document.getElementById('place-details');
  if (placeDetailsSection) {
    // Clear the current content of the place details section
    placeDetailsSection.innerHTML = '';

    // Create elements to display the place details (name, description, price, amenities and reviews)
    const name = document.createElement('h2');
    name.textContent = place.name;

    const description = document.createElement('p');
    description.textContent = place.description;

    const price = document.createElement('p');
    price.textContent = `Price per night: $${place.price}`;

    const amenities = document.createElement('ul');
    place.amenities.forEach(amenity => {
      const amenityItem = document.createElement('li');
      amenityItem.textContent = amenity;
      amenities.appendChild(amenityItem);
    });
    const reviews = document.createElement('div');
    place.reviews.forEach(review => {
      const reviewItem = document.createElement('p');
      reviewItem.innerHTML = `<strong>${review.user}</strong>: ${review.comment}`;
      reviews.appendChild(reviewItem);
    });
    // Append the created elements to the place details section
    placeDetailsSection.appendChild(name);
    placeDetailsSection.appendChild(description);
    placeDetailsSection.appendChild(price);
    placeDetailsSection.appendChild(amenities);
    placeDetailsSection.appendChild(reviews);
  } else {
    console.error('Place details section not found');
  }
}

// ===== ADD REVIEW =====
