import unittest
from app.models import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_fev = User(username="fev",password="123",email="fev@gmail.com",id=1)

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123'))
