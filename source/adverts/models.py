from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


User = get_user_model()


class Adverts(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=2000,
        verbose_name="Описание"
    )
    image = models.ImageField(
        verbose_name="Фото",
        upload_to="advert_foto/",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена',
        validators=(MinValueValidator(0),)
    )
    author = models.ForeignKey(
        User,
        related_name="adverts",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Автор",
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата обновления",
    )
    public_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата обновления",
    )
    is_moderated = models.BooleanField(
        default=False
    )
    status = models.ForeignKey(
        'adverts.Status',
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name="Статус",
        default=1,
    )
    category = models.ForeignKey(
        'adverts.Category',
        related_name='category',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name="Категория",
        default=1,
    )

    def __str__(self):
        return f"{self.pk}. {self.title}."

    class Meta:
        db_table = 'adverts'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Status(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Category(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
