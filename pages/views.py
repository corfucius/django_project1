from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    #[:3] only shows three listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #we bring in these dictionaries from listings/choices.py to be used on pages/index.html

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    #this return passes the listings into the html to be processed
    return render(request, 'pages/index.html', context)

  
def about(request):
    #Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
