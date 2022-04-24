from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Rent)
class RA(admin.ModelAdmin):
    """
    房租Admin
    """
    list_filter = ('status',)
    # The column name that the list displays
    list_display = ('house', 'user', 'create_at', 'start_at', 'months', 'status', 'money', 'price', 'end_at', 'create_at', 'rent_type', 'parent')

@admin.register(Unsubscribe)
class USA(admin.ModelAdmin):
    """
    延期admin
    """
    list_display = ('rent', 'create_at', 'status', 'update_at')
