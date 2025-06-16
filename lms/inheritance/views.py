from django.shortcuts import render

# Create your views here.
def demo(requests):
    return render(requests, 'demo_inheritance/demo.html')

