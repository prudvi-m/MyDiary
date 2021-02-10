from django.urls import path
from .views import DiaryView

urlpatterns = [
    path('home/',DiaryView.as_view()), 
]