// select element with id and assign var
const toggleButton = document.querySelector('#toggle_header');
toggleButton.onclick = switchClass;

// attach event handler
function switchClass() {
  let element = document.getElementsByTagName('header')[0];
  element.classList.toggle('red');
  element.classList.toggle('green');
}
