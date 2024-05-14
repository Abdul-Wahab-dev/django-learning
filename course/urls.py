from course import views
from django.urls import path

urlpatterns = [
    path('', views.index ),
    path('test/', views.test ),
]