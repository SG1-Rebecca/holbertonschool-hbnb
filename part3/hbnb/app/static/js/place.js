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

    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(
        `${API_BASE_URL}/api/v1/places/${placeId}`,
        { headers }
    );

    if (!response.ok) {
        document.getElementById('place-details').innerHTML =
            '<p>Error loading place</p>';
        return;
    }

    const data = await response.json();

    displayPlaceDetails(data);
    displayReviews(data.reviews || []);
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

function displayReviews(reviews) {
    const section = document.getElementById('reviews');

    section.innerHTML = '<h2>Reviews</h2>';

    reviews.forEach(r => {
        const div = document.createElement('div');
        div.className = 'review-card';

        div.innerHTML = `
            <p><strong>${r.user?.first_name || 'Anonymous'}</strong></p>
            <p>${'⭐'.repeat(r.rating || 0)}</p>
            <p>${r.text}</p>
        `;

        section.appendChild(div);
    });
}
