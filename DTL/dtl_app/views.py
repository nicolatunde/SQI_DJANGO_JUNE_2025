from django.shortcuts import render

def dtl(requests):
    context ={
        'username': 'nico',
        'no_of_message': '5',
        'messages': ['hello','free to chat','when can we talk'],
        'is_logged_in': True

    }
    return render(requests,'dtL/dtl-html.html',context)
# Create your views here.
