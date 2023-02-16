from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    job_title = models.CharField(max_length=120)
    job_description = models.TextField()
    job_publish = models.DateTimeField(default=timezone.now)
    job_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'm_job'  #specify table name in db
        ordering = ['-job_publish']  # sort  job

    def __str__(self):
        return self.job_title

