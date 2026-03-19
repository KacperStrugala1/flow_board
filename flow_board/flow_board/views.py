from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .serializers import TaskSerializer

class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        tasks = Task.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"tasks": tasks})

    def post(self, request):
        task = Task.objects.create(
            name = request.POST.get("task_name"),
            description = request.POST.get("task_description"),
            category = request.POST.get("task_category")
        )
        return redirect("home_view")
    
class TaskView(View):
    template_name = "task.html"

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        
        
        return render(request, self.template_name, {"task":task})
    
class HomeRestView(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer
    