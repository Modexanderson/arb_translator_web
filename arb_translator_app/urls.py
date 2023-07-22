from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('arb_translator_app/', views.translation_view, name='translator'),
     path('about/', views.about_view, name='about'),
    # path('contact/', contact_view, name='contact'),
]