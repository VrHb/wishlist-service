from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse

from .forms import WishForm


User = get_user_model()


class Wishlist(models.Model):
    '''Список желаний'''
    user = models.ForeignKey(
        User,
        related_name='wishlists',
        on_delete=CASCADE
    )
    title = models.CharField(
        'Названий списка',
        max_length=100,
        blank=True,
        null=True
    )


    def get_absolute_url(self):
        return reverse('wishlist', kwargs={'wishlist_id': self.pk})

class Wish(models.Model):
    '''Желание пользователя'''
    wishlist = models.ForeignKey(
        Wishlist,
        related_name='wishes',
        on_delete=CASCADE,
        null=True
    )
    title = models.CharField(
        'Название желания',
        max_length=250
    )
    link = models.CharField(
        'Ссылка',
        max_length=300,
        blank=True,
        null=True
    )
    price = models.DecimalField(
        'Цена', 
        max_digits=9, 
        decimal_places=2,
        blank=True,
        null=True
    )
    is_given = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self):
        return self.title

class Gift(models.Model):
    '''Выбранные подарки'''
    title = models.CharField(
        'Название подарка',
        max_length=250
    )
    link = models.CharField(
        'Ссылка',
        max_length=300,
        blank=True,
        null=True
    )
    price = models.DecimalField(
        'Цена', 
        max_digits=9, 
        decimal_places=2,
        blank=True,
        null=True
    )
    wish_id = models.IntegerField(
        'Идентификатор желания',
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        related_name='gifts',
        on_delete=CASCADE
    )

