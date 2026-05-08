from django.db import models

class RobotStatus(models.Model):
    last_message = models.CharField(max_length=500, default="Waiting for robot...")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Status: {self.last_message}"
