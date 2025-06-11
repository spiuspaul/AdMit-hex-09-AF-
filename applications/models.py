from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Application(models.Model):
    StatusChoices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    student = models.CharField(max_length=100)
    status = models.CharField(StatusChoices, default='pending', max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)
    admission_letter = models.FileField(
        upload_to='admission_letters/',
        validators=[FileExtensionValidator(allowed_extensions='pdf')],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        ordering = ['name']

