from django.urls import path
from .api.auth import registration, login

urlpatterns = [
    path('users/registration', registration),
    path('users/login', login),
]
 
from django.urls import path
from .views import upload_file

urlpatterns = [
  path('upload/', upload_file, name='upload_file'),
]