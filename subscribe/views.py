from django.shortcuts import render, redirect
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("valid form")
            print(subscribe_form.cleaned_data)
            email = subscribe_form.cleaned_data["email"]
            first_name = subscribe_form.cleaned_data["first_name"]
            last_name = subscribe_form.cleaned_data["last_name"]
            print(email)
            sb = Subscribe(first_name=first_name, last_name=last_name,
                           email=email)
            sb.save()
            return redirect(reverse("thank_you"))
    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)


def thank_you(request):
    context = {}
    return render(request, "subscribe/thank_you.html", context)
