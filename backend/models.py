from django.db import models
from django.db.models import Sum
from django.forms import model_to_dict
from datetime import timedelta


class Base(models.Model):
    name = models.CharField(max_length=125, verbose_name="nombre")
    is_active = models.BooleanField(default=True, verbose_name="activo")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def to_json(self):
        try:
            return model_to_dict(self)
        except (KeyError, ValueError):
            return {}


class Person(models.Model):
    first_name = models.CharField(max_length=125, verbose_name="nombres")
    last_name = models.CharField(max_length=125, verbose_name="apellidos")
    number_id = models.CharField(max_length=14, verbose_name="número de cédula")
    address = models.TextField(max_length=255, verbose_name="dirección")
    phone_number = models.CharField(max_length=8, verbose_name="número de teléfono")
    date_of_bird = models.DateField(verbose_name="fecha de nacimiento", null=False, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Building(Base):

    @property
    def total_classrooms(self):
        return ClassRoom.objects.filter(floor__in=Floor.objects.filter(building=self)).count()

    total_classrooms.fget.short_description = "Total de salones"

    class Meta:
        verbose_name = "edificio"


class Floor(Base):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors', verbose_name="edificio")

    class Meta:
        verbose_name = "piso"


class ClassRoom(Base):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='número de piso',
                              related_name="classrooms_by_floor", null=True)

    class Meta:
        verbose_name = "salon"
        verbose_name_plural = "salones"


class Shift(Base):
    class Meta:
        verbose_name = "turno"


class ProfessorType(Base):
    class Meta:
        verbose_name = "tipo de profesór"
        verbose_name_plural = "tipos de profesóres"


class Professor(Person):
    professor_type = models.ForeignKey(ProfessorType, on_delete=models.PROTECT, verbose_name="tipo de profesór")

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"


class Student(Person):
    class Meta:
        verbose_name = "estudiante"


class Program(Base):

    class Meta:
        verbose_name = 'programa'

    @property
    def duration(self):
        return timedelta(weeks=self.course_set.all().aggregate(Sum('weeks'))['weeks__sum'] or 0).days / 365


class Course(Base):
    program = models.ForeignKey(Program, on_delete=models.PROTECT, verbose_name="programa")
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, verbose_name="Profesor",
                                  null=True)
    cost = models.FloatField(default=0.0, verbose_name="precio del curso")
    weeks = models.PositiveSmallIntegerField(default=5, verbose_name="duracción en semanas del curso")

    class Meta:
        verbose_name = "curso"

    def to_json(self):
        o = super().to_json()
        if self.id:
            o['professor'] = str(self.professor)
        return o


class Enrollment(Base):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="estudiante")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name="carrera")


class Grades(Base):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="matricula")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="curso", null=True)
    grade = models.IntegerField(default=0, verbose_name="nota")
