from django.urls import path

from . import views
from .views import index,about

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='coin'),
    path('/', index, name='coin'),
    path('about/', about, name='coin'),
]
