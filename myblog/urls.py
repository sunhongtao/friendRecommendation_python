"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns
from django.contrib import admin
from blog import views
from myblog import settings

urlpatterns = patterns('',
#     (r'^collected_static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    (r'^collected_static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^admin/', admin.site.urls),
    url(r'^show', views.show),
    url(r'^$', 'blog.views.login'),
    url(r'^top/$', 'blog.views.top'),
    url(r'^user/$', 'blog.views.showContent'),
    url(r'^test/$', 'blog.views.test'),
    url(r'^recommend', 'blog.views.recommends'),
)



# urlpatterns = [
#     (r'^collected_static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
#     url(r'^admin/', admin.site.urls),
#     url(r'^show',views.show),
#     url(r'^$', 'blog.views.login'),
# ]
