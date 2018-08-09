
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^page/', include('page.urls'), name="page"),
    url(r'^admin/', admin.site.urls),
    url(r'^', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),
]