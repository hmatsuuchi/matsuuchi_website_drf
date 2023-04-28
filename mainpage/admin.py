from django.contrib import admin

from .models import UserProfile, TechnicalSkills, Projects, ProjectDetails

admin.site.register(UserProfile)
admin.site.register(TechnicalSkills)
admin.site.register(Projects)
admin.site.register(ProjectDetails)