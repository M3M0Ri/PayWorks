from django.shortcuts import render
from subscribe.models import Subscribe


def subscribe(request):
    email_error_empty = ""
    if request.POST:
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        print("POST REQUEST : ", email)
        if email == "":
            email_error_empty = "No Email entered"

        sb = Subscribe(first_name=first_name, last_name=last_name,
                       email=email)
        sb.save()
    context = {"email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)
