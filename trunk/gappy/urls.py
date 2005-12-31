from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^gappy/', include('gappy.apps.foo.urls.foo')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls.admin')),
    (r'^accounts/login/', 'gappy.apps.gappy.views.login'),
    (r'^accounts/logout/', 'gappy.apps.gappy.views.logout'),
    (r'^gappy/$', 'gappy.apps.gappy.views.index'),
    (r'^gappy/group/$', 'gappy.apps.gappy.views.group'),
    (r'^gappy/instructor/$', 'gappy.apps.gappy.views.instructor')
)
