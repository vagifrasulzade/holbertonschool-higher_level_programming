#!/usr/bin/node
const character = document.querySelector("#character");

(async function() {
    
    const res = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    const data = await res.json()
    console.log(data);
    character.textContent = data.name;
})();