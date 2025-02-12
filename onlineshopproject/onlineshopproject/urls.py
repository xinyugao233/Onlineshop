"""
URL configuration for onlineshopproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
#
# def log(request):
#     import logging
#
#     # 创建日志记录器
#     logger = logging.getLogger('django')
#     # 输出日志
#     logger.debug('~')
#     logger.info('user logged in')
#     logger.error('user not exist')
#     logger.warning('redis')
#     return HttpResponse('log')

from utils.converters import UsernameConverter
from django.urls import register_converter
register_converter(UsernameConverter, 'username')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.verifications.urls')),
]
