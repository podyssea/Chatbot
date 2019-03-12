from django.urls import path

from . import views

urlpatterns = [
    path('', views.webhook, name='webhook'),
    path('webhook', views.webhook, name='webhook')
]
