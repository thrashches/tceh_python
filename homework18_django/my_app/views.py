from django.shortcuts import render
from django.http import HttpResponse
from my_app.forms import GuestForm

# Create your views here.
#def hello_world(request):
 #   return HttpResponse('Hello, world!')
posts = {}

def index(request):
    if request.method == "POST":
        form = GuestForm(data=request.POST)
        print(form.data['username'])

        posts[form.data['username']] = form.data['text']
    return render(request, 'app/index.html',
                  {'title': 'Гостевуха', 'posts': posts}
                  )