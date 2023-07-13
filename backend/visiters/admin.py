from django.contrib import admin
from .models import Visiter
# Register your models here.
@admin.register(Visiter)
class VisiterAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ("age", "gender",)
    list_filter = ['age','gender']
    

# @admin.register(Count)
# class CountAdmin(admin.ModelAdmin):
#     pass