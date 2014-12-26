from django.conf.urls import patterns, url
from recommendation import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'post/$',views.post,name='post'),
    url(r'category/(?P<category_name>[a-z]+)/$',views.category,name="category")
)