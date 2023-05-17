from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('showdata/', views.ShowStatus, name='showdata'),
    path('post/', views.PostData, name='post'),

]