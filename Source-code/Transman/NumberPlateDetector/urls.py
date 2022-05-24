from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # url(r'^$', views.button),
    url(r'^index', views.index, name="script"),
    url(r'^cars/',views.carList.as_view())
    # path('', views.index, name='index'),
]