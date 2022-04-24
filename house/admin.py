from django.contrib import admin
from .models import *
# Register your models here.

# TODO 更换Logo

admin.site.site_header = 'House Booking System'
admin.site.site_title = 'House Booking System'


# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # Search box at the top of the list page
    search_fields = ('name',)
    # Filter bar on the right side of the list page
    list_filter = ('status',)
    # The column name that the list displays
    list_display = ('name', 'bed_num', 'post_code', 'area', 'position', 'price', 'create_at', 'status', )

@admin.register(HouseImages)
class HIA(admin.ModelAdmin):
    """
    房屋图片
    """
    list_filter = ('house', )
    list_display = ('house', 'picture', )

@admin.register(Comments)
class CA(admin.ModelAdmin):
    """
    评论
    """
    list_filter = ('house', )
    list_display = ('house', 'user', 'content', 'label', 'score', 'create_at')
