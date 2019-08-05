from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('add_payout/', views.add_payout),
]
