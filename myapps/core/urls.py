from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.savesport, name='save_sport_data'),
    path('api/sportnew/', views.savesport_api, name='save_sport_data_api'),
]
