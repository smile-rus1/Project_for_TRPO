from django.db import models

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%M/%d/")  # записывает в раздельные папки по классификаторам

    def __str__(self): # Возвращает название статьи в админке и не только
        return self.title
