const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterTag = document.querySelector('#character');

async function fetchChar() {
  // fetch data from url
  const response = await fetch(URL);
  // parse JSON response
  const data = await response.json();
  // display
  console.log(data);
  // update text content of var char name
  characterTag.textContent = data.name;
}

fetchChar();
