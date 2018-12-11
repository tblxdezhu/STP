from django.contrib import admin
from .models import Machine, Data


# Register your models here.


class MachineAdmin(admin.ModelAdmin):
    list_display = ('ip', 'machine_id', 'process_num', 'output_path')
    search_fields = {'ip'}


admin.site.register(Machine, MachineAdmin)
admin.site.register(Data)
