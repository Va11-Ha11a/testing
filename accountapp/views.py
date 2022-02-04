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

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        Corgi_list = Corgi.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'corgi_list': Corgi_list})
