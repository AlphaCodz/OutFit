from django.urls import path
from .views import SignUpCustomer

urlpatterns = [
    path("signup/", SignUpCustomer.as_view(), name="signup")
]

# PMAK-64256f0eb28a9219b6fd6059-060436755db9632cf56c34083f2de4ebaf