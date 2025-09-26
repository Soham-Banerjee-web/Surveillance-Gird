document.addEventListener('DOMContentLoaded', function() {
    const queryForm = document.getElementById('query-form');
    const queryInput = document.getElementById('query-input');
    const responseContainer = document.getElementById('response-container');

    queryForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const query = queryInput.value;

        fetch('/api/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: query })
        })
        .then(response => response.json())
        .then(data => {
            responseContainer.innerHTML = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            responseContainer.innerHTML = 'An error occurred while processing your request.';
        });
    });
});