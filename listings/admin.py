from django.contrib import admin
from .models import Listing
# Register your models here.


# this class adds a list display to the admin page for Listings
class ListingAdmin(admin.ModelAdmin):
    ''' these are preset tuples and add funtionality, such as links, filters
        and tell django which paramenters to display. You must have a comma after tuple with only one parameter
     '''
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    #add searchable fields to admin
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
