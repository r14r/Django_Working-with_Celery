from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('',  include('app_celery.urls'), name='home'),
    path('admin/', admin.site.urls),
]
