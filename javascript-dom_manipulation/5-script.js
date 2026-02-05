#!/usr/bin/node

const header = document.querySelector("header")

document.querySelector("#update_header").addEventListener("click", () => {
    header.textContent = "New Header!!!"
});