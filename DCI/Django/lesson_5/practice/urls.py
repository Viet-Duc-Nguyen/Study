from django.urls import path
from .views import practice_view

urlpatterns = [
    path('practice/', practice_view, name='practice'),
]