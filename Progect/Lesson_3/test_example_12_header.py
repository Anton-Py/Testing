import pytest
import requests
import json


class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        header = response.headers
        assert header["x-secret-homework-header"] == "Some secret value", "There is no x-secret-homework-header in the response"

#  pytest -s Lesson_3/test_example_12_header.py -k "test_header"
