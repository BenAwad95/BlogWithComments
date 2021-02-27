from django.urls import path, include
from .views import dashboard

app_name = 'users'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls'))
]
