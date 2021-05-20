from rest_framework import routers
from django.urls import path
from .views import ListSimpleTableView


urlpatterns = [
    path('table_data/', ListSimpleTableView.as_view(), name='table-data'),
]
