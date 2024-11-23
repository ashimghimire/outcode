"""
URL configuration for outcode1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', views.get_hotels, name='get_hotels'),
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('rooms/', views.get_rooms, name='get_rooms'),
    path('hotel/', views.create_hotel, name='create_hotel'),
    path('booking/', views.create_bookings, name='create_booking'),
    path('room/', views.create_rooms, name='create_room'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/query/<int:pk>/', views.query_room, name='query_room'),
    path('reviews/<int:pk>/', views.get_reviews, name='get_reviews'),
    path('reviews/<int:pk>/detail/', views.reviews_detail, name='reviews_detail'),
    path('reviews/', views.create_reviews, name='create_reviews'),
    path('hotel/<int:pk>/average-rating/', views.calculate_average_hotel_rating, name='calculate_average_hotel_rating'),
    path('cancel-booking/<int:pk>/', views.cancel_bookings, name='cancel_bookings'),
    path('shorter/', include('shortener.urls')),
    path('watch/', include('videostreamer.urls')),
]

if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
