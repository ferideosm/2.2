from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = "DRAFT", "Черновик"


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='creator')
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Favorite', related_name='favorite', blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.id} -- {self.title}"

class Favorite(models.Model):  
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='favorite_adv')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'favorite_adv')

    def __str__(self) -> str:
        return f"{self.user.id} -- {self.user.username}"
