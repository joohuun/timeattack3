from django.shortcuts import redirect, render
from .models import Category, Drink

# Create your views here.


# def home(request):
#     return render(request, '../templates/home.html')


def home(request):
    if request.method == 'GET':
        all_drink = Drink.objects.all().order_by
        return render(request, 'home.html')
    elif request.method == 'POST':
        name = request.POST.get
