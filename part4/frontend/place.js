/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

const API_BASE_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
  const placeId = getPlaceIdFromURL();
  console.log('placeId from URL:', placeId);
  checkAuthentication(placeId);
});

function checkAuthentication (placeId) {
  const token = getCookie('token');
  const addReviewSection = document.getElementById('add-review');

  if (!placeId) {
    console.error('Place ID not found in URL');
    document.getElementById('place-details').innerHTML = '<p>Place ID not found.</p>';
    return;
  }

  if (!token) {
    addReviewSection.style.display = 'none';
    displayPlaceDetails(mockPlaceDetails);
    fetchPlaceDetails(null, placeId); // Fetch place details without authentication
  } else {
    addReviewSection.style.display = 'block';
    // Store the token for later use
    fetchPlaceDetails(token, placeId);
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

function getPlaceIdFromURL () {
  // Extract the place ID from window.location.search
  const extractPlaceId = new URLSearchParams(window.location.search);
  // Return the place ID
  return extractPlaceId.get('id');
}

async function fetchPlaceDetails(token, placeId) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;

  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/places/${placeId}`, {
      method: 'GET',
      headers
    });

    if (response.ok) {
      const data = await response.json();

      console.log(data);
      
      displayPlaceDetails(data);
      displayReviews(data.reviews || []);
    } else {
      console.error('Failed to fetch place details:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching place details:', error);
  }
}

function displayPlaceDetails(place) {
  const placeDetailsSection = document.getElementById('place-details');

  console.log('Display place:', place);
  
  if (!placeDetailsSection) return;


  document.getElementById('place-title').textContent = place.title || 'Untitled';

  placeDetailsSection.innerHTML = `
    <p><strong>Host:</strong> ${place.owner ? `${place.owner.first_name} ${place.owner.last_name}` : 'Information not available'}</p>
    <p><strong>Price per night:</strong> $${place.price || 0}</p>
    <p><strong>Description:</strong> ${place.description || 'No description available.'}</p>
    <p><strong>Amenities:</strong> ${
      place.amenities && place.amenities.length > 0
        ? place.amenities.map(a => typeof a === 'object' ? a.name : a).join(', ')
        : 'No amenities listed'
    }</p>
  `;
}


// ===== MOCK DATA =====
const mockPlaceDetails = {
  id: 1,
  title: 'Beautiful Beach House',
  price: 150,
  description: 'A beautiful beach house with amazing views...',
  amenities: ['WiFi', 'Pool', 'Air Conditioning'],
  reviews: [
    { user: 'Jane Smith', text: 'Great place to stay!', rating: '&#9733;&#9733;&#9733;&#9733;&#9733;' },
    { user: 'Robert Brown', text: 'Amazing location and very comfortable.', rating: '&#9733;&#9733;&#9733;&#9733;&#9734;' }
  ]
};
