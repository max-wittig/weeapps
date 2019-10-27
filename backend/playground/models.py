from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=30, blank=True)
    expire_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
