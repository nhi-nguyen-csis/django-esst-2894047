
# admin.py: Defines how to manage that data through the web interface


from django.contrib import admin #Hey Django, give me your built-in admin dashboard tool
from . import models

# Register your models here.
# Create a settings class for how my Notes should look in admin
# , but for now, just use the basic settings
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Short version - uses defaults
# Put my Notes in admin, use basic defaults
# admin.site.register(models.Notes)

# Long version - with custom settings
# Put my Notes in admin, AND use my custom NotesAdmin settings
admin.site.register(models.Notes, NotesAdmin)