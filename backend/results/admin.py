from django.contrib import admin
from .models import Result, ResultDetailModel
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "drink_kind",
        "drink_count",
        "description",
    )

@admin.register(ResultDetailModel)
class ResultDetailAdmin(admin.ModelAdmin):
    list_display = (
        "drink_name",
        "description",
        "before_result",
    )
# Register your models here.
