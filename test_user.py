"""
Додати для для усіх ролей користувачів перевірку коректності введення логіна та пароля
Покрити тестами всі методи для ролі Admin із валідними даними.
"""

import unittest
import re
from users_methods import Unregistered, Registered
from connection import Connection


class UsersTests(unittest.TestCase):
    # valid data
    VALID_EMAIL = 'pottsjoel@gmail.com'
    VALID_PASSWORD = 'SO8Jfwrc$'
    # invalid data
    INVALID_EMAIL = 'inorrect@@email.com'
    INVALID_PASSWORD = 12345678

    USER_DATA = [{
        "first_name": "Bill",
        "last_name": "Bobb",
        "date_of_bitrth": "02.05.1684",
        "phone": "+803254",
        "address": "Streee1",
        "password": "123",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": "20"
    }]

    def setUp(self):
        # create SuperAdmin
        self.register = Registered(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.unregister = Unregistered()
        # return super().setUp()

    def tearDown(self):
        selector = Connection()._getNextId('users')-1
        selector = f"id = '{selector}'"
        Connection()._deleteData('users', selector)
        return super().tearDown()

    def clear_record(self, table):
        selector = Connection()._getNextId(table)-1
        selector = f"id = '{selector}'"
        Connection()._deleteData(table, selector)

    def test_create_users(self):
        users_val = Registered(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(users_val, Registered)
        print('Test 1.1: pass.')

    def test_create_invalid_Users(self):
        users_inv = Registered(self.INVALID_EMAIL, self.INVALID_PASSWORD)
        email_pattern = re.compile(
            r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$')

        self.assertNotRegex(self.INVALID_EMAIL,
                            email_pattern, 'Incorrect email!')
        self.assertNotIsInstance(self.INVALID_PASSWORD, str,
                                 f'Incorect data type! It must been str but returned {type(self.INVALID_PASSWORD)}')
        self.assertIsInstance(users_inv, Registered)
        print('Test 1.2: pass.')

    def test_add_admin(self):
        response = self.unregister.add_customer(self.USER_DATA)
        self.assertEqual(response, 'Insert done!')
        print('Test 1.3: pass.')
        self.clear_record('users')


if __name__ == '__main__':
    unittest.main()
