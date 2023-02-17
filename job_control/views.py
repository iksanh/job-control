import django.contrib.auth.forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job
from .form import JobForm

# Create your views here.

#data
posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]

@login_required
def create_job(request):
    if request.method == 'GET':
        context = {'form' : JobForm()}
        return render(request, 'jobs/job_form.html', context)
    elif request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.job_author = request.user
            job.save()
            messages.success(request, 'New job has add successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed to add job')
            return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def edit_job(request, id):
    queryset = Job.objects.filter(job_author = request.user)
    job = get_object_or_404(queryset, job_id=id)

    if request.method =='GET':
        context = {'form' : JobForm(instance=job), 'id' : id}
        return render(request, 'jobs/job_form.html', context)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit data succesfully  ')
            return redirect('home')
        else:
            messages.error(request,'Please correct error input')
            return render(request, 'jobs/job_form.html', {'form' : form})

@login_required
def delete_job(request, id):
    queryset = Job.objects.filter(job_author =  request.user)
    job = get_object_or_404(queryset, job_id = id)
    context = {'job' : job}

    if request.method == 'GET':
        return render(request, 'jobs/job_confirm_delete.html', context)
    elif request.method == 'POST':
        job.delete()
        messages.success(request, 'The Job has been delete successfully')
        return redirect('home')


@login_required
def home(request):

    jobs  = Job.objects.all()
    # return HttpResponse('<h1>Hello</h1>')
    context = {
        'jobs' : jobs,
        'title' : 'List Job'
    }

    
    return render(request, "jobs/home.html", context)


def about(request):
    return render(request, "jobs/about.html")