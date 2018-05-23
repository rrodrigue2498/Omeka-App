from django.contrib import admin
from Omeka_app.models import *
from django import forms

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
	pass
admin.site.register(Items, ItemsAdmin)

class CreatorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Creator, CreatorAdmin)

