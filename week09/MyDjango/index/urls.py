from django.urls import path
from . import views

urlpatterns = [
    path('login_fail', views.login_fail),
    path('login_success', views.login_success),
    path('login', views.log_in),
    path('', views.log_in)
]
