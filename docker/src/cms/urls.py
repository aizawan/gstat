from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('resource/',
         views.resource_list,
         name='resource_list'),
    path('resource/<str:disp_mode>',
         views.resource_list,
         name='resource_list'),
    path('resource/add/',
         views.resource_edit,
         name='resource_add'),
    path('resource/mod/<str:resource_name>/',
         views.resource_edit,
         name='resource_mod'),
    path('resource/del/<str:resource_name>/',
         views.resource_del,
         name='resource_del'),
    path('resource/lock/<str:resource_name>/',
         views.resource_lock,
         name='resource_lock'),
    path('resource/unlock/<str:resource_name>/',
         views.resource_unlock,
         name='resource_unlock'),
]
