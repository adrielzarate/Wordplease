from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.FileField(null=True)
    intro = models.TextField(null=True, blank=True)
    post_body = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} ($ {1})'.format(self.title, self.owner)
