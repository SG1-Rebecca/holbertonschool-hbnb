/*
This is a SAMPLE FILE to get you started.
Please, follow the project instructions to complete the tasks.
*/

const API_BASE_URL = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', () => {
    // Execute the authentication check when the DOM is fully loaded
    const reviewForm = document.getElementById('review-form');
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();

  console.log('URL:', window.location.href);
  console.log('PlaceId:', new URLSearchParams(window.location.search).get('id'));

    if (placeId && token) {
        fetch(`${API_BASE_URL}/api/v1/places/${placeId}`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        .then(res => res.json())
        .then(place => {
            document.getElementById('place-title').textContent = `Reviewing: ${place.title}`;
        });
    }    
    
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            // Get review text from form
            const formData = new FormData(reviewForm);
            const reviewText = formData.get('review');
            const rating = formData.get('rating');

            console.log('Review text', reviewText);
            console.log('Rating', rating);

            if (!reviewText || !rating) {
                alert('Please provide both review text and rating.');
                return;
            }
            try {
                const response = await submitReview(token, placeId, reviewText, rating);
                handleResponse(response);
            } catch (error) {
                alert('An error occurred while submitting your review.');
            }
        }

          );
        }
});

function checkAuthentication() {
    const token = getCookie('token');
    if (!token) {
        window.location.href = '/';
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
  const id = extractPlaceId.get('id');
  console.log('Extracted placeId:', id);
  // Return the place ID
  return id;
}



// Make AJAX request to submit review
async function submitReview(token, placeId, reviewText, rating) {
    // Make a POST request to submit review data
    const url = `${API_BASE_URL}/api/v1/places/${placeId}/reviews`;
    // Include the token in the Authorization header
    try {      
        const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ text: reviewText, rating: parseInt(rating) })
      });
    // Send placeId and reviewText in the request body
    // Handle the response
      return response;
    } catch (error) {
      console.error('Error submitting review:', error);
      throw error;
    }
  }

  
function handleResponse(response) {
    if (response.ok) {
        alert('Review submitted successfully!');
        // Clear the form
        document.getElementById('review-form').reset();
    } else {
        alert('Failed to submit review');
    }
}