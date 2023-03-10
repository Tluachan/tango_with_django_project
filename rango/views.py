from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    #Query database to get Category objects, order by likes - as descending, limit 5
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict2 = {'boldmessage' : 'Crunchy, creamy, cookie, candy'}
    return render(request, 'rango/about.html', context=context_dict2)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None         

    return render(request, 'rango/category.html', context=context_dict)
