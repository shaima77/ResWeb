from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Recipe._meta.get_fields()]