from django.shortcuts import render
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("valid form")
    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)
