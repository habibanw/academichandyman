from django.urls import path

from . import views

app_name = 'providers'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('services/<int:provider_id>/', views.provider_detail, name='provider_detail'),
    path('providerAdd/', views.add_provider, name='add_provider'),
    path('rate_provider/<int:provider_id>/', views.rate_provider, name='rate_provider'),
    path('edit_provider/<int:provider_id>/', views.edit_provider, name='edit_provider'),
]
