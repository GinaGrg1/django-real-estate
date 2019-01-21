from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    '''
    This is the main page of the website. We only want 3 properties to display.
    The listings below will query the postgres table Listing, which is created in listings.models
    '''
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all the realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    # Get MVP. Seller of the month.
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
