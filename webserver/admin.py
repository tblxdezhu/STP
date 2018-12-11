from django.contrib import admin
from .models import Machine, Data

# Register your models here.

admin.site.register(Machine)
admin.site.register(Data)


class MachineAdmin(admin.ModelAdmin):
    list_display = {'ip', 'process_num', 'output_path'}
    search_fields = {'ip'}
