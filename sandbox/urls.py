from django.conf.urls import url

from dummyapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
