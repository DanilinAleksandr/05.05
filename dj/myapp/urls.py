from django.urls import path
from .views import index, week, month, year

urlpatterns = [
    path('', index, name='index'),
    path('week/<int:client_id>', week, name='week'),
    path('month/<int:client_id>', month, name='month'),
    path('year/<int:client_id>', year, name='year'),
]
