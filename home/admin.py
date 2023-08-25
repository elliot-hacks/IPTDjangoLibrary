from django.contrib import admin
from .import models

# Register your models here.
"""
def mark_as_not_borrowed(modeladmin, request, queryset):
    queryset.update(available_copies=F('total_copies'))

"""
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'arthor', 'cover', 'available', 'description']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','description']