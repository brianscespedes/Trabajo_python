from django.contrib import admin
from .models import *


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'is_active')
    search_fields = ('name',)
    list_filter = ('building',)
    fields = ('name', 'building', 'is_active')


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'is_active')
    search_fields = ('name',)
    list_filter = ('floor',)
    fields = ('name', 'floor', 'is_active')


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(ProfessorType)
class ProfessorTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'number_id', 'phone_number')
    list_filter = ('professor_type',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'number_id', 'phone_number')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
