const updateHeaderButton = document.querySelector('#update_header');

updateHeaderButton.onclick = updateHeader;

function updateHeader() {
  let element = document.querySelector('header');
  element.textContent = 'New Header!!!';
}
