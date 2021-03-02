from django.urls import path, include
from .views import dashboard, register

app_name = 'users'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('account/', include('django.contrib.auth.urls')),
    path('register_new/', register, name='register')
]
