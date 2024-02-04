const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.querySelector('#list_movies');

async function fetchMovieTitles() {
  const response = await fetch(URL);
  const data = await response.json();
  // extract titles from fetched data
  const movieTitles = data.results;

  // iterate through each title and append to movie list
  for (const movieTitle of movieTitles) {
    // create new li element for each title
    const newTitle = document.createElement('li');
    // set text content of li element tyo current title
    newTitle.textContent = movieTitle.title;
    // append the li element to the list
    movieList.appendChild(newTitle);
  }
}

fetchMovieTitles();
