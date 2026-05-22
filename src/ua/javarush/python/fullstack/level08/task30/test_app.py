# Testing the Registration API
#
# Write a test for a Flask API that checks the successful registration
# of a new user.
# Use Flask-Testing to create a test database.
# The API must return the correct status code after registration.
# Run the tests using unittest.
#
# Requirements:
#
# 1. The test must use Flask-Testing to create a test database
#    that will be used during test execution.
# 2. The test must verify that the API allows a new user
#    to be registered successfully.
# 3. The API must return the correct status code
#    after successful registration.
# 4. The tests must be implemented and executed
#    using the unittest framework.
#
# 🇺🇦 Ukrainian version:
#
# Тестування API реєстрації
#
# Напишіть тест для Flask API, який перевіряє успішну реєстрацію
# нового користувача.
# Використовуйте Flask-Testing для створення тестової бази даних.
# API має повертати правильний статус код після реєстрації.
# Запустіть тести за допомогою unittest.
#
# Вимоги:
#
# 1. Тест повинен використовувати Flask-Testing для створення тестової бази даних,
#    яка буде використовуватись під час виконання тесту.
# 2. Тест повинен перевіряти, що API дозволяє успішно
#    зареєструвати нового користувача.
# 3. API має повертати правильний статус код
#    після успішної реєстрації.
# 4. Тести мають бути реалізовані та виконані
#    з використанням фреймворку unittest.

import unittest
from flask_testing import TestCase
from app import app, users

class TestRegistrationAPI(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        users.clear()  # Clear users list before each test

    def test_successful_registration(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'User registered successfully'})

    def test_registration_without_username(self):
        response = self.client.post('/register', json={
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Username and password required'})

    def test_duplicate_registration(self):
        # First registration should succeed
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Duplicate registration should fail
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json, {'message': 'User already exists'})

if __name__ == '__main__':
    unittest.main()