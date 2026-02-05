#!/usr/bin/node


const list_movies = document.querySelector("#list_movies");
(async function() {
    
    const res = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const datas = await res.json()
    console.log(datas);
    
    for (data of datas.results) {
        let li = document.createElement("li");
        li.textContent = data.title;
        list_movies.append(li)
    }
})();