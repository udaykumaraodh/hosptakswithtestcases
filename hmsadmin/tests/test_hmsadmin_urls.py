from django.urls import reverse,resolve
from django.test import TestCase

class TestUrls:

    def test_url_sales2admin(self):

        path=reverse('hmadmin')
        assert resolve(path).view_name == 'hmadmin'
