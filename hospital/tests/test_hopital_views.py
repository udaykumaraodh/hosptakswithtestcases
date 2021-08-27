from mixer.backend.django import mixer
import pytest
from django.urls import reverse
from hospital.models import PreRegHos,Sales


from hospital.views import preRegHos
@pytest.mark.django_db
class TestMyView:

    def test_get_hosp(self,rf, api_client):
        mixer.blend('hospital.PreRegHos')
        #request = rf.get(reverse('viewall'))
        print('---------')
        response=api_client.get(reverse('preghos'))
        print(response)
        assert  response.status_code == 200

    def test_post_hospital(self,rf,api_client):
        mixer.blend('hospital.PreRegHos')
        print('====')

        request = rf.get(reverse('preghos'))
        sdata = Sales.objects.create(name="john", dob='1996-02-04', gender="Male", mobile=9632587410,emailId="john123@gmail.com", qualificaton="MCA", address="indore")



        #viewmet = PreRegHos(request)
        sdata=PreRegHos.objects.create(hospital_name="Mediplus",h_address="banjarahills",mobile=9654568125,allocate_to=sdata).save()
        response=api_client.post(reverse('preghos'),data=sdata)
        print(response)
        assert response.status_code == 200


    # def test_put_hospital(self,rf,api_client):
    #     mixer.blend('hospital.PreRegHos')
    #     sdata = Sales.objects.create(name="john", dob='1996-02-04', gender="Male", mobile=9632587410,emailId="john123@gmail.com", qualificaton="MCA", address="indore")
    #     obj, created = PreRegHos.objects.create(hospital_name="Mediplus", h_address="medchal",
    #                                                       mobile=8546971230, allocate_to=sdata)
    #
    #
    #
    #     created.save()
    #     response = api_client.put(reverse('preghos'), data=obj)
    #     assert response.status_code == 200

        #obj,created=PreRegHos.objects.update_or_create(hospital_name="Mediplus",h_address="medchal",mobile=8546971230,allocate_to=sdata)




