from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
    path("contact_me/", views.contact_me, name="contact_me")
]