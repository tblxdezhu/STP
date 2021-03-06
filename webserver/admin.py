from django.contrib import admin
from .models import Machine, Data


# Register your models here.


class MachineAdmin(admin.ModelAdmin):
    list_display = ('ip', 'machine_id', 'process_num', 'code_path', 'output_path', 'data_path',)
    search_fields = ('ip',)


class DataAdmin(admin.ModelAdmin):
    list_display = ('area', 'camera', 'data_path', 'gps_skeleton_path', 'tag', 'data_type')


admin.site.register(Machine, MachineAdmin)
admin.site.register(Data, DataAdmin)
