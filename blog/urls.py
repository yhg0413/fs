
from django.urls import path, re_path
from blog.views import *

urlpatterns =[
    path('admin/', PostLV.as_view(), name='index'),
]