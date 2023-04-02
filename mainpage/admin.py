from django.contrib import admin

from .models import UserProfile, TechnicalSkills

admin.site.register(UserProfile)
admin.site.register(TechnicalSkills)