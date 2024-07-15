from django.urls import path
from core.views import *

app_name="core"

urlpatterns = [
    path('', index),
    path('about/',about ),
    path('contact/', contact),
    path('traker/', traker),
    path('search/',search ),
    path('productview/<int:myid>', productview),
    path('checkout/', checkout),
]
