from django.test import TestCase
from .models import Mymodel
# Create your tests here.


class MymodelTestCases(TestCase):
    def setUp(self):

        Mymodel.objects.create(name="vinayak", email="gaikwad@gmail.com",
                               phone=2147483647)
        Mymodel.objects.create(name="anand", email="anand@gmail.com", phone=1)

    def test_create_success(self):
        vinayak_name = Mymodel.objects.get(name__icontains="vinayak")
        anand_name = Mymodel.objects.get(name__icontains="anand")
        self.assertEqual(vinayak_name.name, "vinayak")
        self.assertEqual(anand_name.name, "anand")

    def test_update_success(self):
        vinayak_name = Mymodel.objects.get(name__icontains="vinayak")
        vinayak_name.phone = 8
        vinayak_name.name = "mrVinayak"
        vinayak_name.email = "vinayak@gmail.com"

        vinayak_name.save()
        self.assertEqual(vinayak_name.phone, 8)
        self.assertEqual(vinayak_name.email, "vinayak@gmail.com")
        self.assertEqual(vinayak_name.name, "mrVinayak")

    def test_delete_success(self):
        vinayak_name = Mymodel.objects.get(name__icontains="Vinayak")
        vinayak_name.delete()
        is_exists = Mymodel.objects.filter(name__icontains="Vinayak").exists()
        self.assertEqual(is_exists, False)
