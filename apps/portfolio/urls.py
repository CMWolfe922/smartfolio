from django.contrib import admin
from django.urls import path, include
# import the views that are needed
from .views import IndexView, PortfolioView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
