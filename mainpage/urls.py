from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.index, name="index"),

    path('api/technical_skills', views.TechnicalSkills.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)