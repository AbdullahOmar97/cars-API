from django.test import TestCase
from django.contrib.auth.models import User
from .models import Car


# Create your tests here.

class CarTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.car = Car.objects.create(model="Model S", brand="Tesla", price=79999.99, is_bought=False)

    def test_car_creation(self):
        self.assertEqual(self.car.model, "Model S")
        self.assertEqual(self.car.brand, "Tesla")
        self.assertEqual(self.car.price, 79999.99)
        self.assertFalse(self.car.is_bought)
