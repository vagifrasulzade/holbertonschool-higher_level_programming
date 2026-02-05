#!/usr/bin/node

const add_item_btn = document.querySelector("#add_item");
let myList = document.querySelector(".my_list");
add_item_btn.addEventListener("click", () => {
  let li = document.createElement("li");
  li.textContent = "Item";
  myList.append(li);
});