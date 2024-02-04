// select element with id and assign to var
const header = document.querySelector('#red_header');
// attach function to click event of header element
header.onclick = changeRed;

function changeRed() {
  let element = document.getElementsByTagName('header')[0];
  element.style.color = '#FF0000';
}
