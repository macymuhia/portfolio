from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(blank=True, default="")
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    github_url = models.URLField()
    linked_in_url = models.URLField()
    twitter_url = models.URLField()


class Menu(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=255)


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    project_url = models.URLField()


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField()


class ProjectTech(models.Model):
    project = models.ForeignKey(
        Project, related_name="technologies", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
