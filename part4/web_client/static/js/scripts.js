document.addEventListener("DOMContentLoaded", () => {
  /* LOGIN */
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        await loginUser(email, password);
      } catch (error) {
        alert("Login failed: " + error.message);
      }
    });
  }

  async function loginUser(email, password) {
    // const url = "https://your-api-url/api/v1/auth/login";
    const url = "https://jsonplaceholder.typicode.com/posts";
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/; Secure; HttpOnly`;
        window.location.href = "index.html";
      } else {
        alert("Login failed: " + response.statusText);
      }
    } catch (error) {
      alert("Login failed: " + error.message);
    }
  }
});

function getCookie(name) {
  const cookies = document.cookie.split("; ");
  const cookie = cookies
    .find((c) => c.startsWith(name + "="));
  return cookie ? decodeURIComponent(cookie.split("=")[1]) : null;
}

function setCookie(name, value, days) {
  const date = new Date();
  date.setDate(date.getDate() + days);
  const cookieString = `${name}=${encodeURIComponent(
    value
  )}; expires=${date.toUTCString()}; path=/; Secure; SameSite=Strict`;
  document.cookie = cookieString;
}
