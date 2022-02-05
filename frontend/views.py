from django.shortcuts import render, HttpResponseRedirect
from backend.models import *
from .forms import *
from django.urls import reverse


def index(request):
    return render(request, 'frontend/index.html', {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
    })


def matriculas(request):
    return render(request, 'frontend/matriculas.html', {
        'matriculas': Student.objects.all(),
    })


def nueva_matricula(request):
    form = MatriculaForm
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('frontend:matriculas'))
    return render(request, 'frontend/nueva-matricula.html', {
        'form': form,
    })
