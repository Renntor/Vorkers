from django.contrib import admin
from .models import Worker, Brigade


@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'specialization')
