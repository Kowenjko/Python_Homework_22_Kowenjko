"""
Додати для для усіх ролей користувачів перевірку коректності введення логіна та пароля
Покрити тестами всі методи для ролі Admin із валідними даними.
"""

import unittest
import re
from admin_methods import Admin, SuperAdmin
from connection import Connection


class SuperAdminTests(unittest.TestCase):
    # valid data
    VALID_EMAIL = 'opa@mail.dog'
    VALID_PASSWORD = '123fff$FG'
    # invalid data
    INVALID_EMAIL = 'inorrect@@email.com'
    INVALID_PASSWORD = 12345678

    ADMIN_DATA = [{
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
        self.super_admin = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        # return super().setUp()
        pass

    def tearDown(self):
        selector = Connection()._getNextId('users')-1
        # self.super_admin.delete_admin(selector)
        return super().tearDown()

    def clear_record(self, table):
        selector = Connection()._getNextId(table)-1
        self.super_admin.delete_admin(selector)

    def test_create_SuperAdmin(self):
        super_admin_val = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(super_admin_val, SuperAdmin)
        print('Test 1.1: pass.')

    def test_create_invalid_SuperAdmin(self):
        super_admin_inv = SuperAdmin(self.INVALID_EMAIL, self.INVALID_PASSWORD)
        email_pattern = re.compile(
            r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$')

        self.assertNotRegex(self.INVALID_EMAIL,
                            email_pattern, 'Incorrect email!')
        self.assertNotIsInstance(self.INVALID_PASSWORD, str,
                                 f'Incorect data type! It must been str but returned {type(self.INVALID_PASSWORD)}')
        self.assertIsInstance(super_admin_inv, SuperAdmin)
        print('Test 1.2: pass.')

    def test_add_admin(self):
        response = self.super_admin.add_admin(self.ADMIN_DATA)
        self.assertEqual(response, 'Insert done!')
        print('Test 1.3: pass.')
        self.clear_record('users')


class AdminTests(unittest.TestCase):
    # valid data
    VALID_ADMIN_EMAIL = 'bil@mail.ru'
    VALID_ADMIN_PASSWORD = 'Windoffs1$'

    # invalid data
    INVALID_ADMIN_EMAIL = 'inorrect@@email.com'
    INVALID_ADMIN_PASSWORD = 12345678

    CATEGORY_DATA = [{
        'category_name': "wardrobe"
    }]

    def setUp(self):
        self.admin = Admin(self.VALID_ADMIN_EMAIL, self.VALID_ADMIN_PASSWORD)

    def tearDown(self):
        selector = Connection()._getNextId('users')-1
        selector = f"id = '{selector}'"
        Connection()._deleteData('product_category', selector)
        return super().tearDown()

    def clear_record(self, table):
        selector = Connection()._getNextId(table)-1
        selector = f"id = '{selector}'"
        Connection()._deleteData(table, selector)

    def test_create_Admin(self):
        admin_val = Admin(self.VALID_ADMIN_EMAIL, self.VALID_ADMIN_PASSWORD)
        self.assertIsInstance(admin_val, Admin)
        print('Test 2.1: pass.')

    def test_create_invalid_Admin(self):
        admin_inv = Admin(self.INVALID_ADMIN_EMAIL,
                          self.INVALID_ADMIN_PASSWORD)
        email_pattern = re.compile(
            r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$')

        self.assertNotRegex(self.INVALID_ADMIN_EMAIL,
                            email_pattern, 'Incorrect email!')
        self.assertNotIsInstance(self.INVALID_ADMIN_PASSWORD, str,
                                 f'Incorect data type! It must been str but returned {type(self.INVALID_ADMIN_PASSWORD)}')
        self.assertIsInstance(admin_inv, Admin)
        print('Test 2.2: pass.')

    def test_add_pr_category(self):
        response = self.admin.add_pr_category(self.CATEGORY_DATA)
        self.assertEqual(response, 'Insert done!')
        print('Test 2.3: pass.')
        self.clear_record('product_category')

    def test_edit_pr_category(self):
        edit = self.admin.edit_pr_category(
            self.CATEGORY_DATA[0], "category_name = 'water'")
        self.assertEqual(edit, 'Update done!')
        print('Test 2.4: pass.')

    def test_edit_pr_category(self):
        dele = self.admin.delete_pr_category('wardrobe')
        self.assertEqual(dele, 'Item was deleted!')
        print('Test 2.5: pass.')

    def test_get_order_info(self):
        info = self.admin.get_order_info(
            category='date_of_order', selector='2021-09-2')
        self.assertTrue(info, 'Is not data!')
        print('Test 2.6: pass.')

    def test_get_order_info_none(self):
        info = self.admin.get_order_info(
            category='date_of_order', selector='2021-09-3')
        self.assertFalse(info, 'The data is there!')
        print('Test 2.7: pass.')


if __name__ == '__main__':
    unittest.main()
