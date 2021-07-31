from django.test import SimpleTestCase
from django.urls import reverse, resolve
from urlshortner.views import shorten_url, shorten_url_next

class TestUrls(SimpleTestCase):
    def test_short_url(self):
        url = reverse('shorten_url', args=["akshay.com"])
        self.assertEquals(resolve(url).func, shorten_url)
       
    def test_short_url_next(self):
        url = reverse('shorten_url_next', args=["akshay1.com"])
        self.assertEquals(resolve(url).func, shorten_url_next)