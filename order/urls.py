from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<id>', OrderView.as_view()),
]
