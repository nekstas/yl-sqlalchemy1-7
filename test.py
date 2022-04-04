# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import datetime

import requests

BASE_URL = 'http://127.0.0.1:5000/api/'


def test_get(url):
    print(requests.get(BASE_URL + url).json())


def test_post(url, json):
    print(requests.post(BASE_URL + url, json=json).json())


def test_delete(url):
    print(requests.delete(BASE_URL + url).json())


def test_put(url, json):
    print(requests.put(BASE_URL + url, json=json).json())


# test_get('jobs')
# test_get('jobs/1')
# test_get('jobs/10000000000')
# test_get('jobs/nekstas')

# # Корректный запрос 1
# test_post('jobs', {
#     'collaborators': '1',
#     'end_date': datetime.datetime.now().isoformat(),
#     'is_finished': False,
#     'job': 'job_k',
#     'start_date': datetime.datetime.now().isoformat(),
#     'team_leader': 1,
#     'work_size': 16
# })
#
# # Корректный запрос 2
# test_post('jobs', {
#     'collaborators': '1',
#     'end_date': None,
#     'is_finished': True,
#     'job': 'job_{k+1}',
#     'start_date': None,
#     'team_leader': 1,
#     'work_size': 24
# })
#
# # Корректный запрос 3
# test_post('jobs', {
#     'collaborators': '1',
#     'end_date': None,
#     'is_finished': False,
#     'job': 'job_{k+2}',
#     'start_date': None,
#     'team_leader': 1,
#     'work_size': 10
# })
#
# # Некорректный запрос 1
# # Вообще ничего не передано (Empty request)
# test_post('jobs', {})
#
# # Некорректный запрос 2
# # Не передан параметр collaborators (Bad request)
# test_post('jobs', {
#     'end_date': None,
#     'is_finished': False,
#     'job': 'job1',
#     'start_date': None,
#     'team_leader': 1,
#     'work_size': 16
# })
#
# # Некорректный запрос 3
# # end_date не None и не в нормальном формате (информация есть, но она неправильного типа) (Invalid data)
# test_post('jobs', {
#     'collaborators': '1',
#     'end_date': '1234',
#     'is_finished': False,
#     'job': 'job1',
#     'start_date': None,
#     'team_leader': 1,
#     'work_size': 16
# })
#
# test_get('jobs')

# # Корректный, если есть работа с id=1
# test_delete('jobs/1')
#
# # Некорректный, если нет работы с id=10000000000
# test_delete('jobs/10000000000')
#
# # Некорректный, не число
# test_delete('jobs/nekstas')
#
# test_get('jobs')

# # Корректный 1, если есть работа с id=2
# test_put('jobs/2', {
#     'work_size': 10
# })
#
# # Корректный 2, если есть работа с id=3
# test_put('jobs/3', {
#     'work_size': 14,
#     'end_date': datetime.datetime.now().isoformat(),
#     'job': 'job3.333'
# })
#
# # Некорректный 1, если нет работы с id=10000000000 (Not Found)
# test_put('jobs/10000000000', {
#     'work_size': 14,
#     'end_date': datetime.datetime.now().isoformat(),
#     'job': 'job3.333'
# })
#
# # Некорректный 2, нет данных для изменения (Empty request)
# test_put('jobs/5', {})
#
# # Некорректный 3, если есть работа c id=1, дата в неверном формате (Invalid date)
# test_put('jobs/5', {
#     'end_date': '1234'
# })
