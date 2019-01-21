from django.apps import AppConfig

# this listings is the name of the table in postgres? This is why we can do {% for listing in listings %} in 
# templates/listings/listings.html ?

class ListingsConfig(AppConfig):
    name = 'listings'
