from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TechnicalSkills as TechnicalSkillsModel
from .models import Projects as ProjectsModel
from .models import ProjectDetails as ProjectDetailsModel
from .serializers import TechnicalSkillsSerializer, ProjectsSerializer, ProjectDetailsSerializer, RelatedTechnologiesSerializer


class TechnicalSkills(APIView):
    def get(self, request, format=None):
        skills_all = TechnicalSkillsModel.objects.all().order_by('skill_type', 'skill_title')

        skills_choices = TechnicalSkillsModel.skill_type.field.choices
        oldest_skill = skills_all.order_by('skill_start').first().skill_start

        serializer = TechnicalSkillsSerializer(skills_all, many=True)

        return Response({'skills_list': serializer.data, 'skills_type_list': skills_choices, 'oldest_skill': oldest_skill})
    
class Projects(APIView):
    def get(self, request, format=None):
        projects_all = ProjectsModel.objects.all().order_by('project_title')

        serializer = ProjectsSerializer(projects_all, many=True)

        return Response(serializer.data)
    
class ProjectDetails(APIView):
    def get(self, request, id, format=None):
        project = ProjectsModel.objects.get(id=id)
        project_details = ProjectDetailsModel.objects.filter(related_project=project).order_by('details_order')
        related_technologies = project.project_technologies.all()

        project_serializer = ProjectsSerializer(project, many=False)
        project_details_serializer = ProjectDetailsSerializer(project_details, many=True)
        related_technologies_serializer = RelatedTechnologiesSerializer(related_technologies, many=True)

        return Response({'project': project_serializer.data, 'project_details': project_details_serializer.data, 'related_technologies': related_technologies_serializer.data})