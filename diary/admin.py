from django.contrib import admin
from .models import Record

# Админка для модуля
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        'content',
        'media',
        'created_at',
        'updated_at',
        'owner',
    )
