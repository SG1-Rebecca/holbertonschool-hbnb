/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

const API_BASE_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
  const placeId = getPlaceIdFromURL();
  const token = checkAuthentication();
  if (placeId) {
    fetchPlaceDetails(token, placeId);
  } else {
    console.error('Place ID not found in URL');
    document.getElementById('place-details').innerHTML = '<p>Place ID not found.</p>';
  }

  // Handle review form submission
  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const formData = new FormData(reviewForm);
      const reviewText = formData.get('review-text');
      const rating = formData.get('rating');

      if (!reviewText || !rating) {
        alert('Please provide both review text and rating.');
        return;
      }

      try {
        const response = await submitReview(token, placeId, reviewText, rating);
        if (response.ok) {
          alert('Review submitted successfully!');
          reviewForm.reset();
          // Refresh place details to show new review
          fetchPlaceDetails(token, placeId);
        } else {
          alert('Failed to submit review.');
        }
      } catch (error) {
        alert('An error occurred while submitting your review.');
      }
    });
  }
});

function checkAuthentication() {
  const token = getCookie('token');
  const addReviewSection = document.getElementById('add-review');

  if (!token) {
    addReviewSection.style.display = 'none';
  } else {
    addReviewSection.style.display = 'block';
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
      console.log('Fetched place data:', data);
      displayPlaceDetails(data);
      displayReviews(data.reviews || []);
    } else {
      console.error('Failed to fetch place details:', response.statusText);
      document.getElementById('place-details').innerHTML = '<p>Failed to load place details.</p>';
    }
  } catch (error) {
    console.error('Error fetching place details:', error);
    document.getElementById('place-details').innerHTML = '<p>Error loading place details.</p>';
  }
}


// ===== Submit Review =====
async function submitReview(token, placeId, reviewText, rating) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/places/${placeId}/reviews`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({ text: reviewText, rating: parseInt(rating) })
    });
    return response;
  } catch (error) {
    console.error('Error submitting review:', error);
    throw error;
  }
}

// ===== Display Reviews =====
function displayReviews(reviews) {
  const reviewsSection = document.getElementById('reviews');
  
  if (!reviewsSection) return;
  
  // Clear current content
  reviewsSection.innerHTML = '';
  
  // Add reviews title
  const reviewsTitle = document.createElement('h2');
  reviewsTitle.textContent = 'Reviews';
  reviewsSection.appendChild(reviewsTitle);
  
  if (!reviews || reviews.length === 0) {
    const noReviews = document.createElement('p');
    noReviews.textContent = 'No reviews yet. Be the first to review!';
    reviewsSection.appendChild(noReviews);
    return;
  }

  reviews.forEach(review => {
    const reviewItem = document.createElement('div');
    reviewItem.className = 'review';
    reviewItem.innerHTML = `
      <p><strong>${review.user || 'Anonymous'}</strong>: ${review.comment || review.text || 'No comment'}</p>
      ${review.rating ? `<p>Rating: ${review.rating}</p>` : ''}
    `;
    reviewsSection.appendChild(reviewItem);
  });
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

