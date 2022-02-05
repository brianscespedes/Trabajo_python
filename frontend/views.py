from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .forms import *
from django.urls import reverse
from backend.models import _statistics


def index(request):
    return render(request, 'frontend/index.html', {
        'programs': Program.objects.all(),
        'students': Student.objects.all(),
        'statistics_student': _statistics(Course, 'credit'),
        'statistics_course': _statistics(Course, 'credit'),
    })


def matriculas(request):
    return render(request, 'frontend/matriculas.html', {
        'matriculas': Student.objects.all(),
    })


def nueva_matricula(request):
    form = MatriculaForm
    if request.method == "POST":
        if 'get_courses' in request.POST:
            return JsonResponse([x.to_json() for x in Course.objects.filter(program_id=request.POST.get('program'))],
                                safe=False)
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('frontend:matriculas'))
    return render(request, 'frontend/nueva-matricula.html', {
        'form': form,
    })
