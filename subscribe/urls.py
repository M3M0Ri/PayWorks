from django.contrib import admin
from django.urls import path, include
from subscribe import views


urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe"),
    path("thank_you", views.thank_you, name="thank_you")

]


