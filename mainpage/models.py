from django.db import models
import datetime
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user                            = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name_kanji                 = models.CharField(max_length=35, blank=True, null=True)
    first_name_kanji                = models.CharField(max_length=35, blank=True, null=True)
    last_name_katakana              = models.CharField(max_length=35, blank=True, null=True)
    first_name_katakana             = models.CharField(max_length=35, blank=True, null=True)
    last_name_romaji                = models.CharField(max_length=35, blank=True, null=True)
    first_name_romaji               = models.CharField(max_length=35, blank=True, null=True)

    main_page_active                = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
    
class TechnicalSkills(models.Model):
    SKILL_TYPE_CHOICES = [
        (1, 'Languages'),
        (2, 'Frameworks/Libraries'),
        (3, 'Databases'),
        (4, 'Tools'),
    ]
    skill_title                 = models.CharField(max_length=64)
    skill_type                  = models.IntegerField(choices=SKILL_TYPE_CHOICES)
    skill_start                 = models.DateField(default=datetime.date.today)

    @property
    def skill_type_display(self):
        return self.get_skill_type_display()

    def __str__(self):
        return str(self.skill_title) + " - " + str(self.get_skill_type_display())
    
class Projects(models.Model):
    project_title           = models.CharField(max_length=64, blank=True)
    project_subtitle        = models.TextField()
    project_image_url       = models.CharField(max_length=512)
    project_image_alt       = models.TextField()
    project_website         = models.CharField(max_length=128, blank=True)
    project_github          = models.CharField(max_length=128, blank=True)
    project_technologies    = models.ManyToManyField(TechnicalSkills)

    def __str__(self):
        return self.project_title
    
class ProjectDetails(models.Model):
    related_project             = models.ForeignKey(Projects, on_delete=models.CASCADE,)
    details_text                = models.TextField()
    details_image_url           = models.CharField(max_length=512)
    details_image_alt           = models.TextField()
    details_image_description   = models.TextField()
    details_order               = models.IntegerField()

    def __str__(self):
        return str(self.related_project.project_title) + " - " + str(self.details_order)