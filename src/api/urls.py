from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('resource/all',
         views.get_json,
         name='resource_list'),
    path('resource/<str:resource_name>',
         views.get_json,
         name='resource_list')
]