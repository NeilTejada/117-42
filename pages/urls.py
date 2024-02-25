from django.urls import path
from pages import views

urlpatterns = [
    path("test", views.test_view, name="test"),
    path("contact", views.contact_view, name="contact"),
]