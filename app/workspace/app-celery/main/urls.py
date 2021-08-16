from django.contrib import admin
from django.urls import include, path

import debug_toolbar

admin.autodiscover()

urlpatterns = [
    path('',  include('app_celery.urls'), name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
]
