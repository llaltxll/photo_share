from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    # to have the file deleted from ths S3 bucket
    def delete(self):
        self.image.delete(save=False)
        return super().delete()

    def __str__(self) -> str:
        return self.description