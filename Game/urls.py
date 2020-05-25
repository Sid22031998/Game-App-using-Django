from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('snake/', views.snake),
    path('colorgame/', views.ColorGame),
]
