from django.shortcuts import render
from uploadapp.forms import UploadFrom


# Create your views here.

def upload_image(request):
    form = UploadFrom()
    return render(request, "uploadapp/add_image.html", {"form":form})
