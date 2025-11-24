from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
import string, random

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        code = generate_code()

        URL.objects.create(long_url=long_url, short_code=code)

        short_url = request.build_absolute_uri(f'/{code}')

        return render(request, "result.html", {"short_url": short_url})

    return render(request, "index.html")


def redirect_url(request, code):
    try:
        entry = URL.objects.get(short_code=code)
        entry.click_count += 1
        entry.save()
        return redirect(entry.long_url)
    except URL.DoesNotExist:
        return HttpResponse("Invalid URL", status=404)
