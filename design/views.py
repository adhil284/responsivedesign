from django.shortcuts import render

# Create your views here.

def responsivehome(request):
    context = {}
    return render(request, 'design/home.html', context)

def responsiveproduct(request):
    context = {}
    return render(request, 'design/products.html', context)

def responsivepeople(request):
    context = {}
    return render(request, 'design/people.html', context)

def responsivecontact(request):
    context = {}
    return render(request, 'design/contactus.html', context)

