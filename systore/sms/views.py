from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'sms/index.html', context)