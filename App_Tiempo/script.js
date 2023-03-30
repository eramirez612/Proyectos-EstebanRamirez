const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');

search.addEventListener('click',()=>{
    const APIKey = '610f6ca1033a8e3ab6804f8b93d7ea4e';
    const city = document.querySelector('.search-box input').value;

    if(city ==='')
        return;
    fetch('https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={APIKey}').then(response => response.json()).then
    (json => {

        if(json.cod === '404'){
            container.style.height = '400px';
            weatherBox.style.height = 'none';
            weatherDetails.style.height = 'none';
            error404.style.height = 'block';
            error404.classList.add('fadeIn');
            return;
        }
    })
})