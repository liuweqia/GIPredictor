from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "here is index."}

    return render(request, 'gip/index.html', context_dict)

