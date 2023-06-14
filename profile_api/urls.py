from django.urls import path
from profiles.views import ProfileAPIView

urlpatterns = [
    path('api/profiles/', ProfileAPIView.as_view()),
]
