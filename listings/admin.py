from django.contrib import admin

# We can register the listings for the admin area here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    """
    This will display the following fields in the 'listing' page of admin. The list_display_links will add links to id and title.
    """
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
    

admin.site.register(Listing, ListingAdmin)