from django.test import SimpleTestCase
from django.test import Client


class HomePageTest(SimpleTestCase):

    def test_home_page_is_200(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_beef(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'beef')

    def test_home_page_requires_login(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'Login')

# class MyOrdersTest(SimpleTestCase):
    # def test_my_orders_needs_login(self):
    #     c = Client()
    #     response = c.get("/my_orders/")
    #     self.assertEqual(response.status_code, 301)
