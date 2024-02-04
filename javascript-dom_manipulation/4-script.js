const addItem = document.querySelector('#add_item');

addItem.onclick = addLi;

function addLi() {
  let element = document.querySelector('ul.my_list');
  let newLi = document.createElement('li');
  newLi.textContent = 'Item';
  element.appendChild(newLi);
}
