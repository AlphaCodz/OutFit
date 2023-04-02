from django.urls import path, re_path
from . import views

app_name="app"

urlpatterns = [
    path("home", views.index, name="home"),
    re_path(r"^shop/", views.shop, name="shop"),
    re_path(r"^about/", views.about, name="about"),
    re_path (r"^services/", views.services, name="service")
]
