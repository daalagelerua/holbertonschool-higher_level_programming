#!/bin/usr/python3

import requests
import csv


def fetch_and_print_posts():
    res = request.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        posts = res.json()

        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    res = request.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        posts = res.json()