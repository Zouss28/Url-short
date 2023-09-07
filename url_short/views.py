# urlshortenerapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShortenURLForm
from .models import urlShort, ClickEvent
from .utils import shortcode_generator

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']
            shortened_code = shortcode_generator()
            obj, created = urlShort.objects.get_or_create(url = original_url, shortcode = shortened_code) 
            # For example, you can use a library like shortuuid to generate a unique code.
            # Save the original and shortened URLs in the database.
            # Return the shortened URL to the user.
            # Redirect to a success page or display the shortened URL to the user.
            return render(request, 'url_short/shortened.html',{
                'object':obj,
            })
    else:
        form = ShortenURLForm()
    return render(request, 'url_short/home.html', {'form': form})

def url_redirect(request, shortcode):
    obj = get_object_or_404(urlShort, shortcode=shortcode)
    ClickEvent.objects.create_event(obj)
    return redirect(obj.url)

def total_clicks(request, shortcode):
    obj = get_object_or_404(urlShort, shortcode=shortcode)
    return render(request, 'url_short/total_clicks.html',{
        'object':obj
    })