from django.db import models
from django.conf import settings


class Patient(models.Model):
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    name = models.CharField(max_length=255)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ]
    )

    contact = models.CharField(max_length=15)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name