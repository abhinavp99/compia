from django.contrib import admin
from .models import Events,  Notices, Complaints, Staff, Attendance


admin.site.register(Events)
admin.site.register(Notices)
admin.site.register(Complaints)
admin.site.register(Staff)
admin.site.register(Attendance)