"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django1.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from projects.views import index

# from django_views.views import index
# from django_views.views import HomeIndex
from projects.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 函数视图的全局路由配置
    # path('index/', index),

    # 类视图的全局路由配置
    #  path('index/', HomeIndex.as_view()),

    # 子路由的全局路由配置
    path('django_views/', include('django_views.urls')),
    path('projects/', IndexView.as_view())
]