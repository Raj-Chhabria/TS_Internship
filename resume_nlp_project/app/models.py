from django.db import models

# Create your models here.

class ResumeData(models.Model):
    Category = models.CharField(max_length=500)
    Resume = models.TextField()
    Raw_html = models.TextField()
    Clean_Resume = models.TextField()
    skills = models.TextField()