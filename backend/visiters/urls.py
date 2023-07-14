from django.urls import path
from . import views

urlpatterns = [
    path("",views.AllVisiters.as_view()),
<<<<<<< HEAD
=======
    # path("counts/",views.Counts.as_view()),
>>>>>>> 0f72ee030948cd426dd102df9338d0d358bffc5c
]