from django.urls import path, include

urlpatterns = [
    path('customers/', include('djoser.urls')),
    path('customers/', include('djoser.urls.authtoken')),
]
