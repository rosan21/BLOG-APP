from django.urls import path
from content_app import views


urlpatterns = [
   path('home/', views.home, name = 'home')
]