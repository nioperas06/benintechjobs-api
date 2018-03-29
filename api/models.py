from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=255)
    email = models.EmailField()
    url = models.URLField()
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.FileField(upload_to='media', blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__():
        return self.title