from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    index_image = models.FileField(upload_to="index_images/", blank=True)
    project_image = models.FileField(upload_to="project_images/", blank=True)
    source_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    documentation_file = models.FileField(upload_to="project_documentation/",blank=True)
    powerbi_iframe_url = models.URLField(blank=True)
    powerbi_description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
