from django.contrib import admin
from .models import Post,ContactMessage
admin.site.register(Post)
admin.site.register(ContactMessage)

# Register your models here.
# admin.py


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
