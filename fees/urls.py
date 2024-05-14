from django.urls import path
from fees import views

urlpatterns = [
    path('' , views.fees_index)
]