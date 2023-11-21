import unittest
from criando_connection import Connection


class TestConnection(unittest.TestCase):
    def test_init(self):
        c = Connection()
        self.assertEqual(c.host, "localhost")
        self.assertEqual(c.port, "80")
        self.assertIsNone(c.user)
        self.assertIsNone(c.password)

    def test_set_user(self):
        c = Connection()
        c.set_user("luiz")
        self.assertEqual(c.user, "luiz")

    def test_set_password(self):
        c = Connection()
        c.set_password("<PASSWORD>")
        self.assertEqual(c.password, "<PASSWORD>")

    def test_connect(self):
        c = Connection()
        self.assertIsNone(c.connect())


if __name__ == "__main__":
    unittest.main()
