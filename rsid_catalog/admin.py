from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ("rs_id",)


admin.site.register(models.Rsids, NotesAdmin)
