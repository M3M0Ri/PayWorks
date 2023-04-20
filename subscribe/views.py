from django.shortcuts import render


def subscribe(request):
    context = {}
    return render(request, "subscribe/subscribe.html", context)
