from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/index.html")

def customer_page(request):
    return render(request, "core/customer.html")

def courier_page(request):
    return render(request, "core/courier.html")