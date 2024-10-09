from django.urls import path
from . import views

urlpatterns = [
    path('flagman/', views.flagman, name = 'flagman'),
]