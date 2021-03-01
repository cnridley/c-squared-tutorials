from django.db import models

# Create your models here.

class PdfUpload(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    fileUpload = models.FileField(upload_to='media/', blank=True)

    def __str__(self):
        return self.title