from django.urls import path, re_path
from . import views

app_name="app"

urlpatterns = [
    path("home", views.index, name="home"),
    re_path(r"^shop/", views.shop, name="shop")
]
