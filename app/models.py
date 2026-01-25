from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    urltag = models.CharField(max_length=1000)
    tag = models.CharField(max_length=1000, default='app')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    info = models.TextField(default="lorem")

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="projects/extra/")

    def __str__(self):
        return f"Imagen de {self.project.name}"
