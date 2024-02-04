// select element
const header = document.querySelector('#red_header');
// attach event handler
header.onclick = changeRed;
// define event handle function
function changeRed() {
  // selects first header element and assigns var
  let element = document.getElementsByTagName('header')[0];
  // sets colour to red
  element.style.color = '#FF0000';
}
