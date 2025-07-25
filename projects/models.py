from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20)
    link = models.URLField()
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    organization = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Project(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='projects/') 
    link = models.URLField(blank=True)
    client = models.CharField(max_length=100, blank=True)
    project_start_date = models.DateField()
    project_end_date = models.DateField(blank=True, null=True)
    summary = models.TextField()

    def __str__(self):
        return self.title

