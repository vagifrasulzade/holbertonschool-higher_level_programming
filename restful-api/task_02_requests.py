#!/usr/bin/python3
"""
Docstring for restful-api.task_02_requests
"""
import requests
import csv
import json

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)
    posts = response.json()
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    response = requests.get(URL)
    if response.status_code == 200:
        posts = response.json()

        formatted_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(formatted_posts)
