from django.shortcuts import render
from helpers.views import BaseView
from .models import Customer
from rest_framework.response import Response
# Create your views here.
class SignUpCustomer(BaseView):
    required_post_fields = ["first_name", "last_name", "email"]
    def post(self, request, format=None):
        super().post(request, format)
        
        email = request.data["email"]
        customer = Customer.objects.filter(email=email).exists()
        if customer:
            resp = {
                "code": 400,
                "message": "Sorry this email is taken"
            }
            return Response(resp, 400)
        
        
        customers = Customer()
        customers.first_name = request.data["first_name"]
        customers.last_name = request.data["last_name"]
        customers.email = request.data["email"]
        customers.save()
        resp = {
            "code": 201,
            "message": f"Welcome to Fashionista {customers.first_name}"
        }
        return Response(resp, 201)