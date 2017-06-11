"""定义simple_blog的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有主题
    url(r'^themes/$', views.themes, name='themes'),
    # 特定主题的页面
    url(r'^themes/(?P<theme_id>\d+)/$', views.theme, name='theme'),
    # 添加新主题的网页
    url(r'^new_theme/$', views.new_theme, name='new_theme'),
    # 添加新内容的页面
    url(r'new_content/(?P<theme_id>\d+)/$', views.new_content, name='new_content'),
    # 编辑内容页面
    url(r'^edit_content/(?P<content_id>\d+)/$', views.edit_content, name='edit_content'),
]