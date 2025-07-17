from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'contact'

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact-us'),
    path('thank-you/', TemplateView.as_view(template_name='contact/thank_you.html'), name='thank-you'),
]
