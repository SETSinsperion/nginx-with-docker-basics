document.getElementById('helloButton').addEventListener('click', () => {
    fetch('http://localhost/api/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = data.msg;
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('healthButton').addEventListener('click', () => {
    fetch('http://localhost/api/health')
        .then(response => {
            if (response.status === 200) {
                document.getElementById('response').innerText = 'Healthcheck passed!';
            } else {
                document.getElementById('response').innerText = 'Healthcheck failed!';
            }
        })
        .catch(error => console.error('Error:', error));
});
