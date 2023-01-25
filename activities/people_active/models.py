from django.db import models

# Create your models here.
from django.urls import reverse


class Activity(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%M/%d/")# записывает в раздельные папки по классификаторам
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    group = models.ForeignKey("Groups", on_delete=models.PROTECT, null=True)

    """
    Возвращает название статьи в админке и не только
    """
    def __str__(self):
        return self.title

    """
    используется в качестве переменной в index.html 
    {{ act.get_absolute_url }} --- возвращает путь
    """
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


class Groups(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    title = models.TextField(blank=True)

    def __str__(self):
        return self.name
