# booking/urls.py
from django.urls import path

from . import views
from .views import book_appointment

app_name = 'booking'
urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]
