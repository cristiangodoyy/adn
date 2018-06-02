from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('mutant/', views.Recruit.as_view()),
    path('stats/', views.Stats.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
