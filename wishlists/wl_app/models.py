from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE


User = get_user_model()

class Wish(models.Model):
    '''Желание пользователя'''
    user = models.ForeignKey(User, related_name='wishes', on_delete=CASCADE)
    title = models.CharField('Название желания', max_length=250)
    text = models.TextField('Описание желания', blank=True, null=True)
    link = models.CharField('Ссылка', max_length=300, blank=True, null=True)
    price = models.DecimalField(
        'Цена', 
        max_digits=7, 
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self):
        return self.title



