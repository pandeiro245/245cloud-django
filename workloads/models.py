from django.db import models
from django.utils import timezone

class Workload(models.Model):
    is_done = models.BooleanField(
        verbose_name='is_done',
        default=False,
    )
    number = models.IntegerField(
        verbose_name='number',
        blank=True,
        null=True,
        default=1,
        # validators=[validators.MinValueValidator(0),
        #             validators.MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(
        verbose_name='created_at',
        blank=True,
        null=True,
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name='updated_at',
        blank=True,
        null=True,
        default=timezone.now
    )
