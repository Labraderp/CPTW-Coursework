document.querySelector('#pic-button').addEventListener('click', loadImage)

async function loadImage() {
    const choice = document.querySelector('#choose-date').value;
    let apiKey = 'https://api.nasa.gov/planetary/apod?api_key=BqYV12QmWheE76RhOg8hw7SLq4rSgekmd6ZGpkAb';
    let url = apiKey + '&date=' + choice;

    let data = await fetch(url);
    let apod = await data.json();

    document.querySelector('img').src = apod.url;
}