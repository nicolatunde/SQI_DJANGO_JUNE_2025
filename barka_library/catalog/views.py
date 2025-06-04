from django.shortcuts import render,HttpResponse

def bool_list(requests):
    return HttpResponse("""<ul>
                        <li>Rich Dad Poor Dad</li>
                        <li>Richest Man In Babylon</li>
                        <li>lovelies</li>
                        <li>my View</li>
                   </ul>""")

# Create your views here.
def special_book(requests):
      return HttpResponse("""<div>
                       <h1>Independence<h1>
                        <h1>The Lord Of The Ring<h1>
                   </div>""")



