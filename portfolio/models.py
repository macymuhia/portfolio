from django.db import models
from fontawesome_5.fields import IconField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile/", default="")
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    github = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_profile(cls):
        return cls.objects.get(pk=1)

    def yearpublished(self):
        return self.pub_date.strftime("%Y")

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=255)

    @classmethod
    def get_all_menus(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    project_url = models.URLField()

    def __str__(self):
        return self.name


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
