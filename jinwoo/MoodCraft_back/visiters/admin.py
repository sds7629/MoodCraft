from django.contrib import admin
from .models import Visiter
# Register your models here.
@admin.register(Visiter)
class VisiterAdmin(admin.ModelAdmin):
    list_display = ("age", "gender",)