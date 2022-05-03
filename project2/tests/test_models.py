from django.test import TestCase


class YourTestClass(TestCase):
    def setUp(self):
        pass
    def test_number_1(self):
        self.assertEqual(2 + 2, 4)
    def test_number_2(self):
        a = 5
        self.assertTrue(a > 4)
    def test_number_3(self):
        b = 6
        self.assertFalse(b > 6)