import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL

# Generate a random short URL (6 characters long)
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# View to shorten the URL
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')

        # Check if the URL is already shortened
        existing_url = URL.objects.filter(original_url=original_url).first()
        if existing_url:
            return HttpResponse(f"Shortened URL: /{existing_url.shortened_url}")

        # Generate a unique short URL
        short_url = generate_short_url()
        while URL.objects.filter(shortened_url=short_url).exists():
            short_url = generate_short_url()

        # Save the original and shortened URL
        new_url = URL(original_url=original_url, shortened_url=short_url)
        new_url.save()

        return HttpResponse(f"Shortened URL -> /{short_url}")
    return render(request, 'shortener/home.html')

# View to redirect to the original URL
def redirect_to_url(request, short_url):
    try:
        url = URL.objects.get(shortened_url=short_url)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return HttpResponse("URL not found", status=404)
