from django.shortcuts import render
from uploadapp.forms import UploadFrom


# Create your views here.

def upload_image(request):
    if request.method == "POST":
        form = UploadFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFrom()
    return render(request, "uploadapp/add_image.html", {"form":form})
