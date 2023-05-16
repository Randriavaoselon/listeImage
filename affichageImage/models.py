from django.db import models
#from PIL import Image

# Create your models here.
class Image(models.Model):
    titre = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200, null=True)
    imgs = models.ImageField(upload_to="pht/%y", null=True)

    def __str__(self):
        return self.titre