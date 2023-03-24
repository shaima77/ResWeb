from django.contrib import admin
from .models import Recipe
from .models import Review

@admin.register(Recipe)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Recipe._meta.get_fields()]

admin.site.register(Review)
