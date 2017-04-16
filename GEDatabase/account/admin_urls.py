from django.conf.urls import url

from .views import dashboard

urlpatterns = [
    url(r'^', dashboard, name='dashboard'),
    url(r'^login/$', login, name='login'),
]