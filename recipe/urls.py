from django.urls import path
from . import views


app_name = 'recipe'

urlpatterns = [
    path('test/', views.testPage, name='testPage'),
]
