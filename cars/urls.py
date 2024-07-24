from django.urls import path
from .views import CarListCreate, CarDetailUpdateDelete

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailUpdateDelete.as_view(), name='car-detail-update-delete'),
]