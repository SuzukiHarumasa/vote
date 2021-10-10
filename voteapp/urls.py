from django.urls import path
from . import views

urlpatterns = [
    path('votes', views.VotesView.as_view(),name="votes"),
]