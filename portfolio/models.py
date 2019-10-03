from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile/", default="")
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    email = models.EmailField(default="")
    github = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    handshake = models.ImageField(upload_to="profile/", default="")

    @classmethod
    def get_profile(cls):
        return cls.objects.get(pk=1)

    def yearpublished(self):
        return self.pub_date.strftime("%Y")

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=10)
    url = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255)
    weight = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("weight",)

    @classmethod
    def get_all_menus(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    project_url = models.URLField()
    image = models.ImageField(upload_to="covers/", default="")

    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_single_project(cls, id):
        return cls.objects.get(pk=id)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="screenshots/", default="")

    @classmethod
    def get_images_of_project(cls, id):
        return cls.objects.filter(project_id=id)


class ProjectTech(models.Model):
    project = models.ForeignKey(
        Project, related_name="technologies", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="tech/", default="")

    @classmethod
    def get_all_technologies(cls):
        return cls.objects.all()

    @classmethod
    def get_technologies_of_project(cls, id):
        return cls.objects.filter(project_id=id)


class Quote(models.Model):
    quote = models.TextField(max_length=500)
    author = models.CharField(max_length=20)

    @classmethod
    def get_all_quotes(cls):
        return cls.objects.all()


class SkillCategory(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Skill Categories"

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    def __str__(self):
        return self.category


class Technology(models.Model):
    technology = models.ForeignKey(
        SkillCategory, related_name="skills", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to="technology/", default="")

    class Meta:
        ordering = ("id",)
        verbose_name_plural = "Technologies"

    @classmethod
    def get_technologies_in_category(cls):
        return cls.objects.select_related("technology")

    @classmethod
    def get_all_technologies(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name
