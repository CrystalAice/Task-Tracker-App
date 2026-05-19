from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length = 100)
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'pending'
    )
    body = models.TextField()

    def __str__(self):
        return self.title


