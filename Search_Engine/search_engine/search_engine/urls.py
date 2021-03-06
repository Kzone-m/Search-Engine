"""search_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from practice import views
from .views import AjaxData, scrape, scrape_result,look_up, look_up_result

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^practice_list/$', views.practice_list, name='practice_list'),
    url(r'^practice_add/$', views.practice_add, name='practice_add'),
    url(r'^practice_edit/(\d+)/', views.practice_edit, name='practice_edit'),
    url(r'^practice_delete/(\d+)/', views.practice_delete, name='practice_delete'),
    url(r'^api/ajax/data/$', AjaxData.as_view()),
    url(r'^scrape/$', scrape, name='scrape'),
    url(r'^scrape_result/$', scrape_result, name='scrape_result'),
    url(r'^look_up/$', look_up, name='look_up'),
    url(r'^look_up_result/$', look_up_result, name='look_up_result'),
]
