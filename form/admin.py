from django.contrib import admin

# Register your models here.

from .models import PersonModel


@admin.register(PersonModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number')
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name',)
    list_filter = ('number',)
    