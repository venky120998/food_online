from django.urls import path
from . import views

urlpatterns = [
    path(route='register_user', view=views.register_user, name='register_user')
]