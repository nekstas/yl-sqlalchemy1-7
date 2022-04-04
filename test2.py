# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import datetime

import requests

BASE_URL = 'http://127.0.0.1:5000/api/v2/'


def test_get(url):
    print(requests.get(BASE_URL + url).json())


def test_post(url, json):
    print(requests.post(BASE_URL + url, json=json).json())


def test_delete(url):
    print(requests.delete(BASE_URL + url).json())


def test_put(url, json):
    print(requests.put(BASE_URL + url, json=json).json())


test_delete('users/3')
test_get('users/1')
