from django.urls import reverse,resolve
from django.test import TestCase

class TestUrls:

    def test_url_hospital(self):
        print('hellooo')

        path=reverse('preghos')
        assert resolve(path).view_name == 'preghos'
