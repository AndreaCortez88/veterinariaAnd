from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', About, name='about'),
    path('blog/', Blog, name='blog'),
    path('contact/', Contact, name='contact'),
    path('petguide/', Petguide, name='petguide'),
    path('petmart/', Petmart, name='petmart'),

]
