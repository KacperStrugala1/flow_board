from django.db import models

class Status(models.TextChoices):
    STARTED = "S", "STARTED"
    PROGRESS = "P", "IN PROGRESS"
    DONE = "D", "DONE"
    

class Task(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=30)
    status = models.CharField(
        max_length=1,
        choices=Status.choices, 
        default=Status.STARTED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name