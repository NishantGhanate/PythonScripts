from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    #views.function name
    #views.classname.as_view
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:album.id>', views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/$' ,views.DetailView.as_view(),name='detail' )  
]