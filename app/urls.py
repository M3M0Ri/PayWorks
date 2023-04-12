from django.contrib import admin
from django.urls import path
from .views import hello, job_detail, job_list

urlpatterns = [
    path("", job_list, name="jobs_home"),
    path("hello/", hello, name="hello"),
    path("job/<int:id>", job_detail, name="jobs_detail")
]
