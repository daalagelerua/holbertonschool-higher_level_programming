#!/bin/usr/python3

import requests
import csv


def fetch_and_print_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        posts = res.json()

        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        posts = res.json()

        structured_data = []
        for post in posts:
            structured_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", mode='w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)
