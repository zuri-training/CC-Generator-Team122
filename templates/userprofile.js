'use strict';

let userInfo = document.getElementById('user-info');
let dropdown = document.getElementById('hidden');
let close = document.getElementById('close');

userInfo.addEventListener('click', function () {
  dropdown.classList.remove('hide')
});
close.addEventListener('click', function(){
    dropdown.classList.add('hide')
});