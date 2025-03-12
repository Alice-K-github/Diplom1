from django.db import models
from django.db.models import CASCADE
from users.models import CustomUser


# Обозначение не-пустого значения переменных
NULLABLE = {'blank': True, 'null': True}

class Record(models.Model):
    # Посты в приложении
    title = models.TextField(verbose_name='Заголовок', **NULLABLE)
    content = models.TextField(verbose_name='Текст', **NULLABLE)
    media = models.ImageField(upload_to='media/', verbose_name='Можете добавить изображение', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания', help_text='формат "dd.mm.yy"', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', help_text='формат "dd.mm.yy"', **NULLABLE)
    owner = models.ForeignKey(CustomUser, on_delete=CASCADE, verbose_name='Создатель', **NULLABLE)

    # Строковое обозначение
    def __str__(self):
        return f'{self.title} {self.created_at}'

    class Meta:
        verbose_name = 'наименование записи'
        verbose_name_plural = 'наименования записей'
