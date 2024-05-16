from django.urls import path
from enroll import views

urlpatterns = [
    path('signup/' , views.sign_up , name='signup'),
    path('login/' , views.user_login),
    path('dashboard/',views.user_dashboard,name="dashboar"),
    path('logout/',views.user_logout, name='logout'),
    path('changepass/' , views.user_change_pass , name="change_pass")
]