from django.http import HttpResponse
from django.contrib.auth.models import Permission, User
from .models import Events, Notices, Complaints, Staff, Attendance
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ComplaintForm, UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View


def index(request):
    return HttpResponse("<h1 text-align: center > Welcome</h1>");

def events(request):
    records = Events.objects.all()
    context = {'records': records}
    return render(request, 'page/templates/events.html', context)

def members(request):
    records = User.objects.all()
    context = {'records' : records}
    return render(request, 'page/templates/members.html', context)

def notices(request):
    records = Notices.objects.all()
    context = {'records': records}
    return render(request, 'page/templates/notices.html', context)

def complaints(request):
    records = Complaints.objects.all()
    context = {'records': records}
    return render(request, 'page/templates/complaints.html', context)


def staff(request):
    records = Staff.objects.all()
    records2 = Attendance.objects.all()
    context = {'records': records, 'records2' : records2}
    return render(request, 'page/templates/staff.html', context)

def login(request):
    records = Staff.objects.all()
    records2 = Attendance.objects.all()
    context = {'records': records, 'records2' : records2}
    return render(request, 'page/templates/staff.html', context)


class ComplaintCreate(CreateView):
    model = Complaints
    form_class = ComplaintForm
    success_url = '/page/complaints/'

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = '/page/members/'

#def UserLogin(CreateView):
 #   model = User
  #  form_class = UserForm
   # success_url = '/page/members/'





