from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# All the urls created in the apps should be added to this main url.py file

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),  # if anyone hits listing/ it will goto listings.urls
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
