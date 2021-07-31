from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def test_short_url_GET(self):
        client = Client()
        response1 = client.get(reverse('shorten_url_next', args=["akshay.com"]))
        self.assertEquals(response1.status_code, 200)
        response2 = client.get(reverse('shorten_url_next', args=["akshay.com"]))
        self.assertEquals(response2.status_code, 200)
        response3 = client.get(reverse('shorten_url_next', args=["akshayanother.com"]))
        self.assertEquals(response3.status_code, 200)
        self.assertEquals(str(response1.content), str(response2.content))
        self.assertNotEquals(str(response1.content), str(response3.content))
        