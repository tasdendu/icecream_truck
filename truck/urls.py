from django.urls import path
from .views import TruckView

urlpatterns = [
    path('trucks/', TruckView.as_view()),
    path('trucks/<id>', TruckView.as_view())
]
