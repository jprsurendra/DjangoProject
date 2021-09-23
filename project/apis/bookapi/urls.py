from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from apis.bookapi import views

urlpatterns = [
    url("",views.BookApiView.as_view()), #new
]
