from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('flagman/', views.flagman, name = 'flagman'),
    path('flagman/details/<int:id>', views.details, name ='details'),
    path('testing/', views.testing, name='testing'),
]