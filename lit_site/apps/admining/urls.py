from django.urls import path
from . import views

app_name = 'admining'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('leave_appeal/', views.leave_appeal, name = 'leave_appeal')
]
