from django.urls import path
from vehiculo.views import index_View

urlpatterns = [
    path('', index_View, name = 'index')
]