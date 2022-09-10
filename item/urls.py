from django.urls import path
from .views import ItemView, FlavorView

urlpatterns = [
    path('items/', ItemView.as_view()),
    path('items/<id>', ItemView.as_view()),
    path('flavors/', FlavorView.as_view()),
    path('flavors/<id>', FlavorView.as_view()),
]
