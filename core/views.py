from django.shortcuts import render
from .models import Category, Item
from django.contrib.auth.decorators import login_required

@login_required
def items(request):
    items = Item.objects.all()
    search = request.GET.get('category', '')
    if search:
        items = Item.objects.filter(category__title=search)
    categories = Category.objects.all()
    return render(request, 'items.html', {'items': items, 'categories': categories})

@login_required
def categories(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'categories.html', {'categories' : categories} )