from django.shortcuts import render

def index (request):
    return render(None, 'ex00/index.html')