
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect_fraud/', views.detect_fraud, name='detect_fraud'),
]
