#!/usr/bin/node
const header = document.querySelector('header');
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#red_header').addEventListener('click', () => {
        header.style.color = '#FF0000';
        console.log('Header color changed to red');
    });
});
