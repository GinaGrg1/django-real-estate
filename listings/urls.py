from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),  # e.g http://localhost:8000/listings/6
    path('search', views.search, name='search'),
]