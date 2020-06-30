
from django.urls import path
from home.views import (
    home_view,
    contact_us_view,
    services_view,
    shop_view,
    about_us_view,
    )


urlpatterns = [
    path('',home_view, name='home'),
    path('contact_us/',contact_us_view, name='contact_us'),
    path('services/',services_view, name='services'),
    path('shop/',shop_view, name='shop'),
    path('about_us/',about_us_view, name='about_us'),
]