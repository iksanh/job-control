from django.forms import  ModelForm
from .models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields =['job_title', 'job_description']