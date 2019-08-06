from django.urls import path, include
from . import views

app_name="table"

urlpatterns = [
    path('', views.main_page, name="main"),
    path('add_payout/', views.add_payout, name="add"),
]
