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
    const url = 'https://your-api-url/login';
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });
    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/; secure; samesite=strict`;
      window.location.href = 'index.html';
    } else {
      alert('Login failed: ' + response.statusText);
    }

  // Handle the response
}


// USER AUTHENTICATION