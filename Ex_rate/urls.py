from django.urls import path
from .views import home, result

app_name = 'Ex_rate'
urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result')
]