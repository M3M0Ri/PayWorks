from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost


class TempClass:
    x = 5


# Create your views here.
def hello(request):
    template = loader.get_template("app/hello.html")
    list_2 = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    contex = {"name": "M3MORi", "age": 30, "first_list": list_2,
              "temp_object": TempClass, "is_authenticated": is_authenticated}
    # return HttpResponse(template.render(contex, request))
    return render(request, "app/hello.html", contex)


def job_list(request):
    # <ul><li>Job 1</li><li>Job 2</li></ul>
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse("jobs_detail", args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    contex = {"jobs":jobs}
    return render(request, "app/index.html", contex)


job_title = [
    "First job",
    "Second Job",
    "Third Job"
]

jop_description = [
    "First hello description",
    "Second hello description",
    "Third Job description"

]


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        # return_html = f"<h1>{job_title[int(id)]}</h1> " \
        #               f"<h3>{jop_description[int(id)]} </h3>"
        # return HttpResponse(return_html)
        context = {"job_title": job_title[id],
                   "jop_description": jop_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
