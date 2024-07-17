from django.contrib import admin
from tasks.models import (
    TasksManagement,
    TeamMember,
    AssignTask,
    Department
)


# Register your models here.
admin.site.register(TasksManagement)
admin.site.register(TeamMember)
admin.site.register(AssignTask)
admin.site.register(Department)
