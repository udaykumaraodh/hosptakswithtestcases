from mixer.backend.django import mixer
from django.contrib.auth.models import User, AnonymousUser
import pytest
from django.urls import reverse
from sales.views import salesApi,salesViewall
from django.test import RequestFactory
from sales.models import Sales
# import  json




import json

#from django.core.urlresolvers import reverse

from sales.views import salesViewall


@pytest.mark.django_db
class TestMyView:

    def test_result_finished(self,rf, api_client):
        mixer.blend('sales.Sales')
        request = rf.get(reverse('viewall'))
        print('---------')
        viewmet=salesViewall(request)
        response=api_client.get(reverse('viewall'),viewmet)
        print(response)
        assert  response.status_code == 200


    def test_sales_post(self,rf,api_client):
        mixer.blend('sales.Sales')
        print('====')
        request = rf.get(reverse('viewall'))
        viewmet = salesApi(request)
        sdata=Sales.objects.create(name="bhairv",dob='1996-02-04',gender="Male",mobile=9632587410,emailId="bhairv123@gmail.com",qualificaton="MCA",address="indore").save()
        response=api_client.post(reverse('salesadmin'),data=sdata)
        print(response)
        assert response.status_code == 200


    # def test_sales_put(self,api_client,request):
    #     mixer.blend('sales.Sales')
    #     print("*****")
    #     udata = Sales.objects.get(name="bhairv", dob='1996-02-04', gender="Male", mobile=9332587210,emailId="bhairv123@gmail.com", qualificaton="MBA", address="Hyderabad").save()
    #
    #     response=api_client.put(reverse('salesadmin'),data=udata)
    #     assert response.status_code == 200
    #
    #
    def test_sales_delete(self,api_client):
        mixer.blend('sales.Sales')
        print('-----')

        print(id)
        sdata=Sales.objects.get(pk=1)
        response=api_client.delete(reverse('salesadmin'),data=sdata)
        print('deleted')
        assert  response.status_code==200







# @pytest.mark.django_db
# class TestViews:
#     def test_view_sales(self):
#         mixer.blend('sales.Sales')
#         path=reverse('viewall')
#         request=RequestFactory().get(path)
#         request.user=mixer.blend(User)
#         print(request.user)
#
#         response=salesViewall(request)
#         print(salesViewall(request))
#         print(response)
#         assert response.status_code ==200
#
#
#     def test_view_sales_auto(self):
#         mixer.blend('sales.Sales')
#         path=reverse('viewall')
#         request=RequestFactory().get(path)
#         request.user=AnonymousUser()
#         response=salesViewall(request)
#
#         print(response)
#         assert response.status_code == 200





































# import pytest
# from django.urls import reverse
# from pytest_drf import APIViewTest, Returns200, UsesGetMethod,UsesListEndpoint
# from pytest_lambda import lambda_fixture
#
#
#
#
#
# @pytest.mark.django_db
# class TestSalesviews(
#     APIViewTest,
#     UsesGetMethod,
#     UsesListEndpoint,
#         Returns200,
#
# ):
#     key_values = lambda_fixture(
#         lambda: [
#             Sales.objects.create(key=key, value=value)
#             for key, value in {
#                 'quay': 'worth',
#                 'chi': 'revenue',
#                 'umma': 'gumma',
#             }.items()
#         ],
#         autouse=True,
#     )
#
#     def test_it_returns_key_values(self, key_values, results):
#         expected = express_key_values(sorted(key_values, key=lambda kv: kv.id))
#         actual = results
#         assert expected == actual
