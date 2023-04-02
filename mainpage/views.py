from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TechnicalSkills as TechnicalSkillsModel
from .serializers import TechnicalSkillsSerializer


class TechnicalSkills(APIView):
    def get(self, request, format=None):
        skills_all = TechnicalSkillsModel.objects.all().order_by('skill_type', 'skill_title')

        skills_choices = TechnicalSkillsModel.skill_type.field.choices
        oldest_skill = skills_all.order_by('skill_start').first().skill_start

        serializer = TechnicalSkillsSerializer(skills_all, many=True)

        return Response({'skills_list': serializer.data, 'skills_type_list': skills_choices, 'oldest_skill': oldest_skill})