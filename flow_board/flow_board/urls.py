
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home_view"),
    #<int:value> - value the same as value provided to view
    path('task/<int:pk>', views.TaskView.as_view(), name="task_view"),
    path('tasks/', views.TaskApiView.as_view(), name='tasks'),
]
