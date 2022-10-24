from django.contrib import admin

from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'name')
    list_filter = ('user',)


admin.site.register(Task, TaskAdmin)
