from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Building)
class BuildingAdmin(ImportExportModelAdmin):
    list_display = ('name', 'total_classrooms', 'is_active')
    search_fields = ('name',)


@admin.register(Floor)
class FloorAdmin(ImportExportModelAdmin):
    list_display = ('name', 'building', 'is_active')
    search_fields = ('name',)
    list_filter = ('building',)
    fields = ('name', 'building', 'is_active')


@admin.register(ClassRoom)
class ClassRoomAdmin(ImportExportModelAdmin):
    list_display = ('name', 'floor', 'is_active')
    search_fields = ('name',)
    list_filter = ('floor',)
    fields = ('name', 'floor', 'is_active')


@admin.register(Shift)
class ShiftAdmin(ImportExportModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(ProfessorType)
class ProfessorTypeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Professor)
class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'number_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'number_id', 'phone_number')
    list_filter = ('professor_type',)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'number_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'number_id', 'phone_number')


@admin.register(Program)
class ProgramAdmin(ImportExportModelAdmin):
    list_display = ('name', 'duration', 'is_active')
    list_filter = ('is_active',)


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ('name', 'professor', 'weeks', 'program', 'cost', 'credit', 'is_active')
    list_filter = ('program', 'is_active',)
