from django.urls import path

from . import views

urlpatterns = [
    path('start-bot/', views.startBot, name='connect bot'),
]