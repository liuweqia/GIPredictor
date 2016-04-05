from django.shortcuts import render

from models import Category, Page


def index(request):
    context_dict = {}

    context_dict['boldmessage'] = "here is index."
    categories = Category.objects.all()

    context_dict['categories'] = categories

    return render(request, 'gip/index.html', context_dict)


def category(request):
    context_dict = {}

    categories = Category.objects.all()
    pages = Page.objects.filter(category=categories)

    context_dict['categories'] = categories
    context_dict['pages'] = pages

    return render(request, 'gip/category.html', context_dict)


def about(request):
    context_dict = {}
    categories = Category.objects.all()

    context_dict['categories'] = categories

    return render(request, 'gip/about.html', context_dict)











