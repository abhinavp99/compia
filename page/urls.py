from django.conf.urls import url
from . import views
from .models import Events,  Notices, Complaints, Staff, Attendance
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    #/page
    #registering user
    url(r'^$', views.UserCreate.as_view(), name='register'),
    #/page/events/
    url(r'^events/$', views.events, name='events'),
    #/page/members
    url(r'^members/$', views.members, name='members'),
    #/page/notices
    url(r'^notices/$', views.notices, name='notices'),
    #/page/complaints
    url(r'^complaints/$', views.complaints, name='complaints'),
    #/page/complaints/add
    url(r'^complaints/add/$', views.ComplaintCreate.as_view(), name='add'),
    #/page/staff
    url(r'^staff/$', views.staff, name='staff'),
    #/page/login
    #url(r'^login/$', views.login, name='register'),

]