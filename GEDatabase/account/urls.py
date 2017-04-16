from django.conf.urls import url

from django.contrib.auth.views import login
from .views import dashboard

urlpatterns = [
    url(r'^', dashboard, name='dashboard'),
    url(r'^login/$', login, name='login'),
]