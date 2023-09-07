from django.urls import path
from .views import shorten_url, url_redirect, total_clicks

urlpatterns = [
    path('',shorten_url),
    path("<slug:shortcode>/",url_redirect),
    path("total-licks/<slug:shortcode>/",total_clicks, name='total_clicks'),
]