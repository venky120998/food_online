from django.urls import path
from . import views

urlpatterns = [
    path(route='register_user', view=views.register_user, name='register_user'),
    path(route='register_vendor', view=views.register_vendor, name='register_vendor')
]