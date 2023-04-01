
from django.urls import path
from . import views


urlpatterns = [
    path('security', views.security, name="security"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout")
]
