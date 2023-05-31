from django.test import SimpleTestCase
from django.test import Client


# Test for home page functionality
class HomePageTest(SimpleTestCase):

    # Success status on loading homepage
    def test_home_page_is_200(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    # Contains Beef product page
    def test_home_page_contains_beef(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'beef')

    # Contains Lamb product page
    def test_home_page_contains_lamb(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'lamb')

    # Contains Chicken product page
    def test_home_page_contains_chicken(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'chicken')

    # Contains a Login page
    def test_home_page_contains_login(self):
        c = Client()
        response = c.get("/")
        self.assertContains(response, 'Login')


# Test order validation.
class MyOrdersTest(SimpleTestCase):

    # Must be logged in to view basket.
    def test_basket_needs_login(self):
        c = Client()
        response = c.get("/basket/")
        self.assertEqual(response.status_code, 302)

    # Must be logged in to view orders.
    def test_my_orders_needs_login(self):
        c = Client()
        response = c.get("/my_orders/")
        self.assertEqual(response.status_code, 302)
