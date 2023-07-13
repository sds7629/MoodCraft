from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ResultInfo.as_view()),
    path("<int:pk>/detail/", views.ResultDetail.as_view()),
]