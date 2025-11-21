document.addEventListener('DOMContentLoaded', () => {

    // TEST MODE → no authentication needed
    fetchPlacesTest();

    /* Fetch from jsonplaceholder for test */
    async function fetchPlacesTest() {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/posts');
            const data = await response.json();

            // Add FAKE price for filter testing
            const places = data.slice(0, 20).map(item => ({
                name: item.title,
                description: item.body,
                location: "Test City",
                price: Math.floor(Math.random() * 120) + 1 // 1 → 120€
            }));

            displayPlaces(places);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    /* Display places */
    function displayPlaces(places) {
        const placeList = document.getElementById('places-list');
        placeList.innerHTML = '';

        places.forEach(place => {
            const div = document.createElement('div');
            div.classList.add('place-content');

            div.dataset.price = place.price;

            div.innerHTML = `
                <h3><strong>${place.name}</strong></h3>
                <p>${place.description}</p>
                <p><strong>Price:</strong> ${place.price} €</p>
                <p>${place.location}</p>
                <button>View details</button>
            `;

            placeList.append(div);
        });
    }

    /* Filter */
    document.getElementById('price-filter').addEventListener('change', (event) => {

        const selectedPrice = event.target.value;
        const options = document.querySelectorAll('.place-content');

        let maxPrice;

        switch (selectedPrice) {
            case "10":  maxPrice = 10; break;
            case "50":  maxPrice = 50; break;
            case "100": maxPrice = 100; break;
            case "all":
            default: maxPrice = Infinity; break;
        }

        options.forEach(option => {
            const price = parseFloat(option.dataset.price);

            if (price <= maxPrice) {
                option.style.display = "block";
            } else {
                option.style.display = "none";
            }
        });
    });

});
