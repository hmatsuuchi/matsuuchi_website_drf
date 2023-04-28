from rest_framework import serializers
from .models import TechnicalSkills, Projects, ProjectDetails

class TechnicalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkills
        
        fields = [
            'id',
            'skill_title',
            'skill_type',
            'skill_type_display',
            'skill_start',
        ]

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects

        fields = [
            'id',
            'project_title',
            'project_subtitle',
            'project_image_url',
            'project_image_alt',
            'project_website',
            'project_github',
        ]

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails

        fields = [
            'id',
            'related_project',
            'details_text',
            'details_image_url',
            'details_image_alt',
            'details_image_description',
            'details_order',
        ]

class RelatedTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkills

        fields = [
            'id',
            'skill_title',
            'skill_type',
            'skill_start',
        ]