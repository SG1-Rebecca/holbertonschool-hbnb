// LOGIN
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        await loginUser(email, password);
      } catch (error) {
        console.error('Login error:', error);
        alert('Login failed: ' + error.message);
      }
    });
  }
});

async function loginUser(email, password) {
    const url = 'http://127.0.0.1:5000/api/v1/auth';
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();
      // Store JWT token in a cookie
      document.cookie = `token=${data.access_token}; path=/; secure; samesite=strict`;

      // Redirect to main page
      alert('Login successful!');
      window.location.href = 'index.html';
    } else {
      alert('Login failed: ' + response.statusText);
    }

  // Handle the response
}


// USER AUTHENTICATION