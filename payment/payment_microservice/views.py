from django.shortcuts import render

# Create your views here.


def payment_page(request):
    return render(request, 'payment_microservice/cart.html')
