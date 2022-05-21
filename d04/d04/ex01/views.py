from django.shortcuts import render


def django (request):
    return render(None, 'ex01/django.html')

def display (request):
    return render(None, 'ex01/display.html')

def templates (request):
    return render(None, 'ex01/templates.html')