from django.db import models
from django.utils import  timezone

# Create your models here.

class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    job_title = models.CharField(max_length=120)
    job_description = models.TextField()
    job_start = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'm_job'  #specify table name in db
