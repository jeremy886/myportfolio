from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio_list, name="portfolio_list"),
    path('portfolio/<int:pk>/', views.portfolio_detail, name = 'portfolio_detail'),
]