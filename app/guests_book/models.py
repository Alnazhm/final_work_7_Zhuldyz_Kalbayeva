from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoices(TextChoices):
    ACTIVE = 'Active', 'Активно'
    BLOCKED = 'Blocked', 'Заблокировано'



class Guests(models.Model):
    author = models.CharField(verbose_name='Имя автора', max_length=200, null=False, blank=False)
    email = models.EmailField(verbose_name="Почта автора", max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name="Текст записи", max_length=2000, null=False, blank=False)
    status = models.CharField(verbose_name="Статус", choices=StatusChoices.choices, default=StatusChoices.ACTIVE, max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Время редактирования', auto_now=True)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    def __str__(self):
        return f"{self.author} - {self.email} - {self.description}"

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
