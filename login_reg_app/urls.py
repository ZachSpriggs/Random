from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_reg),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('delete/<str:role>/<int:user_id>', views.delete),
]