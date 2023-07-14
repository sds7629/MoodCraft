from django.urls import path
from . import views

urlpatterns = [
    path("<str:drink_kind>/", views.ResultInfo.as_view()),
    path("<str:drink_kind>/detail/", views.ResultDetail.as_view()),
]