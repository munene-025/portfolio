from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'technologies')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject')
