from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE


class Wishlist(models.Model):
    '''Список желаний'''
    session_id = models.CharField('Идентификатор сессии', max_length=250, blank=True, null=True)
    title = models.CharField('Названий списка', max_length=100, blank=True, null=True)

class Wish(models.Model):
    '''Желание пользователя'''
    wishlist = models.ForeignKey(Wishlist, related_name='wishes', on_delete=CASCADE, null=True)
    title = models.CharField('Название желания', max_length=250)
    link = models.CharField('Ссылка', max_length=300, blank=True, null=True)
    price = models.DecimalField(
        'Цена', 
        max_digits=7, 
        decimal_places=2,
        blank=True,
        null=True
    )
    is_given = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self):
        return self.title

class Gift(models.Model):
    '''Выбранные подарки'''
    session_id = models.CharField('Идентификатор сессии', max_length=250, blank=True, null=True)
    title = models.CharField('Название подарка', max_length=250)
    link = models.CharField('Ссылка', max_length=300, blank=True, null=True)
    price = models.DecimalField(
        'Цена', 
        max_digits=7, 
        decimal_places=2,
        blank=True,
        null=True
    )

