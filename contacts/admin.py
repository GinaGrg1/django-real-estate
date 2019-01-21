from django.contrib import admin
from .models import Contact

# Django has a builtin admin interface that reads metadata from your models, such as fields, and 
# lets you perform CRUD operations for free.
# To be able to perform such operations, you need to register your models in the admin.py file

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)  # Contact is the name of the table. created in models.py