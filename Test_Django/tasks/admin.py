from django.contrib import admin


from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ('check', 'name', 'user', 'type_task', 'priority', 'observation', 'date_start')
    list_filter = ['type_task', 'priority','date_start']
    search_fields = ['name','observation']

admin.site.register(Task, TaskAdmin)

