from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from accountapp.models import Corgi


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('doggo_input')

        welsh_corgi = Corgi()
        welsh_corgi.text = temp
        welsh_corgi.save()

        return render(request, 'accountapp/hello_world.html', context={'corgi_output': welsh_corgi})

    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'Do U like doggo?'})
