from django.urls import path
from django.urls.resolvers import URLPattern
from user import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("login",views.login,name="login")
]