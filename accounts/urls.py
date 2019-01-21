from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),  # full link will be localhost:8000/accounts/login
    path('register', views.register, name='register'),  # full link will be localhost:8000/accounts/register
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')  # full link will be localhost:8000/accounts/dashboard
]

# line 45 from _navbar.html
#  <a class="nav-link" href="{% url 'register' %}"> ... this url should match the above at line 6.
