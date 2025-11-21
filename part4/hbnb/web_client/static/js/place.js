/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    /* Get place ID */
      function getPlaceIdFromURL() {
      // Extract the place ID from window.location.search
      // Your code here
  }
  /* Check user auth */
    function checkAuthentication() {
      const token = getCookie('token');
      const addReviewSection = document.getElementById('add-review');

      if (!token) {
          addReviewSection.style.display = 'none';
      } else {
          addReviewSection.style.display = 'block';
          // Store the token for later use
          fetchPlaceDetails(token, placeId);
      }
  }

  function getCookie(name) {
      // Function to get a cookie value by its name
      // Your code here
  }
  /* Fetch place details */
    async function fetchPlaceDetails(token, placeId) {
      // Make a GET request to fetch place details
      // Include the token in the Authorization header
      // Handle the response and pass the data to displayPlaceDetails function
  }
  });