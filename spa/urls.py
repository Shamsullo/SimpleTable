
from django.contrib import admin
from django.urls import path, include
from table.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('table.api.urls')),
    path('', index)
]
