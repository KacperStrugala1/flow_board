from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TaskSerializer

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

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.status = request.POST.get("statuses")
        task.save()
        return redirect("task_view", pk=pk)

class TaskApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)