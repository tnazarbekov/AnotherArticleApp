from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    text = models.CharField('Текст Статьи', max_length=300)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/articles/{self.id}'
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
