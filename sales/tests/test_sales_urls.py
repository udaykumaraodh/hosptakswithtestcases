from django.urls import reverse,resolve
from django.test import TestCase

class TestUrls:

    def test_url_sales(self):
        print('hellooo')
        #print(reverse('salesadmin'))
        path=reverse('salesadmin')
        assert resolve(path).view_name == 'salesadmin'

        #assert 10 == 10

    def test_url_sales_viewal(self):
        path=reverse('viewall')
        assert  resolve(path).view_name == 'viewall'


