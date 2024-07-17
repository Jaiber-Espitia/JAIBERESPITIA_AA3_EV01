from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('delete/<str:pk>', view=views.delete_task, name="delete"),
    path('tasks/', view=views.task_manager, name="tasks"),
    path('add/', view=views.add_task, name="add"),
    path('update/<str:pk>', view=views.update_task, name="update"),
    path('endTask/<str:pk>', view=views.task_is_finished, name="is_finished"),

    # Asignar tareas
    path('assignTask/', view=views.assign_task, name="assign_task"),
    path('assignNewTask/', view=views.assign_new_task, name="assign_new_task"),
    path('deleteAssignedTask/<str:pk>', view=views.delete_an_assigned_task, name="delete_assigned_task"),
    path('finalizeAssignedTask/<str:pk>', view=views.finalize_an_assigned_task, name="finalize_assigned_task"),
    path('updateAssignedTask/<str:pk>', view=views.update_assigned_task, name="update_assigned_task"),
   


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)