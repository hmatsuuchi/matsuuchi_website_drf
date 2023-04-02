from rest_framework import serializers
from .models import TechnicalSkills

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