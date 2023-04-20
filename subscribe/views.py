from django.shortcuts import render


def subscribe(request):
    email_error_empty = ""
    if request.POST:
        email = request.POST["email"]
        print("POST REQUEST : ", email)
        if email == "":
            email_error_empty = "No Email entered"
    context = {"email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)
