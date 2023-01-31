from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Activity(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст", null=True)
    photo = models.ImageField(upload_to="photos/%Y/%M/%d/", verbose_name="Фото", null=True)# записывает в раздельные папки по классификаторам
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    group = models.ForeignKey("Groups", on_delete=models.PROTECT, verbose_name="Группы")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

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
        """
        Возвращает по слагу который определен в маршрутах
        """
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name_plural = "События"
        ordering = ["-update_date", "create_date","title"]


class Groups(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    title = models.TextField(blank=True, verbose_name="Текст")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_group", kwargs={"group_slug": self.slug})

    class Meta:
        verbose_name_plural = "Группы"
        ordering = ["name"]


class ActivityDiscussion(models.Model):
    message = models.CharField(max_length=30, db_index=True, verbose_name="Сообщение")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("discussion", kwargs={"discussion_slug": self.slug})

    class Meta:
        verbose_name_plural = "Сообщения"
        ordering = ["-message"]
