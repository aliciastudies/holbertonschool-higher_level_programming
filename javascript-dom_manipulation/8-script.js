document.addEventListener('DOMContentLoaded', function () {
  async function fetchHello() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const element = document.getElementById('hello');
    const response = await fetch(url);
    const data = await response.json();

    element.textContent = data.hello;
  }

  fetchHello();
});
