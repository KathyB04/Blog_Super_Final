from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^', include(('blog.urls', 'blog'), namespace = "blog")), 
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
