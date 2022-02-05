from backend.models import *
from django import forms
from .widgets import *


class MatriculaForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), label="Programa de estudios/Carrera")
    courses = forms.Field(label="Cursos incluidos en el programa", required=False,
                          widget=CoursesWidget)

    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].widget.attrs['choices'] = Course.objects.all()
