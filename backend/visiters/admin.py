from django.contrib import admin
from .models import Visiter,Count
# Register your models here.
@admin.register(Visiter)
class VisiterAdmin(admin.ModelAdmin):
    # list_display = ("age", "gender",)
    pass

@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    pass