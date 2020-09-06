from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments_info, name='comments_info'),
    # path('/', views.comments_info),
    # path('phones/', views.comments_info),
]
