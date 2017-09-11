from django.conf.urls import url
from .views import PostDetail

app_name = 'posts'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='detail'),
]