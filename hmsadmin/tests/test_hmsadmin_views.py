from mixer.backend.django import mixer
import pytest
from django.urls import reverse
from hmsadmin.models import Sales2Admin
from  hospital.models import PreRegHos,Sales
from sales.models import Sales
from hmsadmin.models import Sales2Admin

from hmsadmin.views import hmsAdmin
@pytest.mark.django_db
class TestMyView:

    def test_sales2admin_get(self,rf, api_client):
        mixer.blend('hmsadmin.Sales2Admin')

        print('---------')
        sdata = Sales.objects.create(name="john", dob='1996-02-04', gender="Male", mobile=9632587410,emailId="john123@gmail.com", qualificaton="MCA", address="indore")

        print(sdata.name)
        sa = Sales2Admin.objects.get(salesperson__name=sdata.name)
        response=api_client.get(reverse('hmadmin'),data=sa)
        print(response)
        assert  response.status_code == 200

    def test_post_hmsadmin(self,rf,api_client):
        mixer.blend('hmsadmin.Sales2Admin')
        print('====')

        request = rf.get(reverse('hmadmin'))
        sdata = Sales.objects.create(name="john", dob='1996-02-04', gender="Male", mobile=9632587410,emailId="john123@gmail.com", qualificaton="MCA", address="indore")
        print(sdata.address)
        #viewmet = PreRegHos(request)
        print("--helo")
        hs=PreRegHos.objects.create(hospital_name="Mediplus",h_address="banjarahills",mobile=9654568125,allocate_to=sdata)
        print(hs,'----ff')
        sa=Sales2Admin.objects.create(salesperson=sdata,hopital=hs,mob2=9632587410,address2="gachibowli",city="hyderabad").save()

        response=api_client.post(reverse('hmadmin'),data=sa)
        print(response)
        assert response.status_code == 200

