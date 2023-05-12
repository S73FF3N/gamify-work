from django.shortcuts import render
from .models import Task, CompletedTask

def landing_page(request):
    # Get the 10 most recently completed tasks
    recently_completed_tasks = CompletedTask.objects.order_by('-completion_date')[:10]
    
    # Get the 5 most recently added tasks
    recently_added_tasks = Task.objects.order_by('-creation_date')[:5]
    
    context = {
        'recently_completed_tasks': recently_completed_tasks,
        'recently_added_tasks': recently_added_tasks
    }
    
    return render(request, 'landing_page.html', context)
