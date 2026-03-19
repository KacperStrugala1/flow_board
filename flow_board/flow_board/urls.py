
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
#define route 
router = routers.DefaultRouter()
router.register(r"tasks", views.HomeRestView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home_view"),
    #<int:value> - value the same as value provided to view
    path('task/<int:pk>', views.TaskView.as_view(), name="task_view"),
    path('', include(router.urls)),
]
