from django.urls import path
from .views import subscriptions

urlpatterns = [
    path('', subscriptions, name='all_subscription'),
]
