from . import views
from django.urls import path
from .views import taskListView,taskCreateView,CompleteTaskListView,TaskUpdateView,allTaskListView


urlpatterns = [
    path('', allTaskListView.as_view(), name='app-main'),
    path('mytasks/', taskListView.as_view(), name='app-home'),
    path('add/', taskCreateView.as_view(), name='app-add'),
    path('completed/', CompleteTaskListView.as_view(), name='app-done'),
    path('edit/<int:pk>', TaskUpdateView.as_view(), name='app-edit'),
    
]