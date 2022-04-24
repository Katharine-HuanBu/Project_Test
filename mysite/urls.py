from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user.urls'), name='user'), # 用户
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), # 引入ckeditor
    path('captcha/', include('captcha.urls')), # 验证码
    path('', index, name='index'), # 首页

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL) # 配置静态资源的路径