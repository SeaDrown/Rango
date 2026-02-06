from django.urls import path
from rango import views

appName = "rango"

urlpatterns = [
    path("", views.index, name="index")
]