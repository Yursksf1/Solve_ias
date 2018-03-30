from django.contrib import admin


from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ( 'name', 'user', 'type_task', 'priority', 'observation', 'date_start','date_end','duration_lazy','check')
    list_filter = ['type_task', 'priority','date_start']
    search_fields = ['name','observation']

    def duration_lazy(self, obj):
        url = obj.duration_lazy()
        return url
    duration_lazy.admin_order_field = 'date_start'


    #duration_lazy.admin_order_field = 'duration'


admin.site.register(Task, TaskAdmin)

