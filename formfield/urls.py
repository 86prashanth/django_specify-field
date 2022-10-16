from django.urls import path
from .views import *

urlpatterns = [
    path('',showfromdata,name='home'),
    path('success/',success,name='success'),
    path('specify/',collect,name='specify'),
]
