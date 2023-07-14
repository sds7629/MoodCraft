<<<<<<< HEAD
from django.contrib import admin
from .models import Visiter
from results.models import Result,ResultDetailModel
# Register your models here.
@admin.register(Visiter)
class VisiterAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ("age", "gender","result","result_detail")
    list_filter = ['age','gender']
    

=======
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
>>>>>>> 0f72ee030948cd426dd102df9338d0d358bffc5c
