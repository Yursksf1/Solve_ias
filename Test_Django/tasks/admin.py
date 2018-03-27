from django.contrib import admin


from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ('check', 'name', 'user', 'type_task', 'priority', 'observation', 'deadline')
    list_filter = ['type_task', 'priority','deadline']
    search_fields = ['name','observation']

admin.site.register(Task, TaskAdmin)


