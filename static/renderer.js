const inputBox = document.querySelector('textarea');
const outputBox = document.querySelector('#translation');

inputBox.addEventListener('input', () => {
    const text = inputBox.value;

    fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: text })
    })
    .then(response => response.json())
    .then(data => {
        outputBox.value = data.translation;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
