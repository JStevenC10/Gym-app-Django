from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('all/clients/', views.all_clients, name='clients'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("logout/<int:cc>", views.logout, name="logout"),
    path('welcome/<int:cc>/<str:name>/', views.welcome, name='welcome'),
    path('pay/<int:cc>/', views.pay_month, name='pay'),
    path('delete/client/<int:cc>/', views.delete_client, name='delete_client'),
]