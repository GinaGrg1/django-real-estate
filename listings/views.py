from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing  # This is a class created in listings/models.py

# This html is under templates/listings
def index(request):
    # we can do Listing.objects.all() to display all the rows. 
    # We do order by list_date in descending using hyphen. Only show the property with is_published=True
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)  

def listing(request, listing_id):
    # Single listing. E.g when you click on 'More Info' it should take you to the info about that property.
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords. For eg. in the main home page, if we search for 'pool' we should get a response/ad.
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)  # dunder used here. keyword should be in description field.
    
    # Searching by city. This has to be an exact match. iexact means it is case insensitive.
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # Searching by state.
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Searching by no of bedrooms.
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Searching by price.
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # We are adding 'values' here so that after we do a search for e.g pool, that word will still stay there. Add values.city and values.keywords in search.html
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
