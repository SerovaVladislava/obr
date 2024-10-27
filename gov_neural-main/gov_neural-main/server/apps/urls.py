from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('server.apps.system.urls')),
    path('api/', include('server.apps.neural.urls')),
]


from django.urls import path
from gov_neural_main.server.apps.neural.views import upload_file

urlpatterns = [
  path('upload/', upload_file, name='upload_file'),
]