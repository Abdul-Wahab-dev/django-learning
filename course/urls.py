from course import views
from django.urls import path

urlpatterns = [
    path('', views.index ),
    path('test/', views.test ),
    path('success/' , views.success),
    path('<my_id>/' , views.showCourse , {"check":"ok","hello":"world"} ,name='details')
]