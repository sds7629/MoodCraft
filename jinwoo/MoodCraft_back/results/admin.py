from django.contrib import admin
from .models import Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "drink_kind",
        "drink_count",
        "description",
    )
# Register your models here.
